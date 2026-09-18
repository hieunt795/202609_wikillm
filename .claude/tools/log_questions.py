#!/usr/bin/env python3
"""On-demand logger for user prompts stored in exported conversations.

This script is deliberately local and deterministic: it does not call an LLM,
does not run in the background, and writes only when invoked explicitly.

Supported input forms:
1. JSON or JSONL records with role/content fields.
2. Codex rollout JSONL containing session_meta and response_item events.
3. ChatGPT-style conversation exports containing a mapping of messages.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = REPO_ROOT / ".claude" / "local" / "question-logger" / "questions.jsonl"
DEFAULT_SESSIONS_ROOT = Path.home() / ".codex" / "sessions"

SYSTEM_TERMS = (
    "agent",
    "audit",
    "automation",
    "cấu hình",
    "database",
    "debug",
    "deduplicate",
    "git",
    "hook",
    "index",
    "ingest",
    "kiểm thử",
    "logging",
    "metadata",
    "pipeline",
    "plugin",
    "prompt cache",
    "refactor",
    "repository",
    "schema",
    "script",
    "system",
    "test",
    "tool",
    "workflow",
    "vận hành",
    "hệ thống wiki",
)

WIKI_TERMS = (
    "citation",
    "concept",
    "evergreen",
    "knowledge node",
    "nguồn",
    "source",
    "tri thức",
    "wiki",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract user prompts, classify them, deduplicate, and append JSONL."
    )
    parser.add_argument(
        "--input",
        type=Path,
        help=(
            "Process one conversation export or Codex rollout. If omitted, "
            "scan every Codex session belonging to --project-root."
        ),
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=REPO_ROOT,
        help=f"Project used to filter Codex sessions (default: {REPO_ROOT}).",
    )
    parser.add_argument(
        "--sessions-root",
        type=Path,
        default=DEFAULT_SESSIONS_ROOT,
        help=f"Codex sessions directory (default: {DEFAULT_SESSIONS_ROOT}).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Destination JSONL (default: {DEFAULT_OUTPUT}).",
    )
    parser.add_argument("--chat-id", help="Only log messages from this chat ID.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show proposed records without writing the output file.",
    )
    return parser.parse_args()


def normalized_path(path: Path | str) -> str:
    return os.path.normcase(os.path.abspath(os.fspath(path)))


def path_is_in_project(candidate: Any, project_root: Path) -> bool:
    if not isinstance(candidate, str) or not candidate:
        return False
    candidate_path = normalized_path(candidate)
    project_path = normalized_path(project_root)
    try:
        return os.path.commonpath([candidate_path, project_path]) == project_path
    except ValueError:
        return False


def read_session_meta(path: Path) -> dict[str, Any] | None:
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
            if record.get("type") == "session_meta":
                payload = record.get("payload")
                return payload if isinstance(payload, dict) else None
            return None
    return None


def discover_project_rollouts(sessions_root: Path, project_root: Path) -> list[Path]:
    if not sessions_root.is_dir():
        raise ValueError(f"Codex sessions directory does not exist: {sessions_root}")

    matches: list[Path] = []
    for path in sessions_root.rglob("rollout-*.jsonl"):
        meta = read_session_meta(path)
        if not meta:
            continue
        roots = [meta.get("cwd")]
        runtime_roots = meta.get("runtime_workspace_roots")
        if isinstance(runtime_roots, list):
            roots.extend(runtime_roots)
        if any(path_is_in_project(root, project_root) for root in roots):
            matches.append(path)
    return sorted(matches)


def read_input(path: Path) -> Any:
    text = path.read_text(encoding="utf-8-sig")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        records = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
        return records


def text_from_content(content: Any) -> str | None:
    if isinstance(content, str):
        return content
    if isinstance(content, dict):
        if isinstance(content.get("text"), str):
            return content["text"]
        return text_from_content(content.get("parts"))
    if isinstance(content, list):
        parts: list[str] = []
        for part in content:
            value = text_from_content(part)
            if value is not None:
                parts.append(value)
        return "\n".join(parts) if parts else None
    return None


def message_record(
    *,
    role: Any,
    content: Any,
    chat_id: Any,
    message_id: Any = None,
    timestamp: Any = None,
) -> dict[str, Any] | None:
    if role != "user":
        return None
    question = text_from_content(content)
    if question is None or question == "":
        return None
    return {
        "chat_id": str(chat_id) if chat_id is not None else "unknown",
        "message_id": str(message_id) if message_id is not None else None,
        "timestamp": timestamp if timestamp is not None else "unknown",
        "question": question,
    }


def extract_from_mapping(conversation: dict[str, Any]) -> Iterator[dict[str, Any]]:
    chat_id = conversation.get("id") or conversation.get("conversation_id") or "unknown"
    mapping = conversation.get("mapping")
    if not isinstance(mapping, dict):
        return
    for node in mapping.values():
        if not isinstance(node, dict):
            continue
        message = node.get("message")
        if not isinstance(message, dict):
            continue
        author = message.get("author") or {}
        item = message_record(
            role=author.get("role"),
            content=message.get("content"),
            chat_id=chat_id,
            message_id=message.get("id"),
            timestamp=message.get("create_time"),
        )
        if item:
            yield item


def extract_messages(data: Any) -> Iterator[dict[str, Any]]:
    records = data if isinstance(data, list) else [data]
    rollout_chat_id: str | None = None

    for record in records:
        if not isinstance(record, dict):
            continue

        if isinstance(record.get("mapping"), dict):
            yield from extract_from_mapping(record)
            continue

        if record.get("type") == "session_meta":
            payload = record.get("payload") or {}
            rollout_chat_id = payload.get("id") or payload.get("conversation_id")
            continue

        if record.get("type") == "response_item":
            payload = record.get("payload") or {}
            if payload.get("type") != "message":
                continue
            item = message_record(
                role=payload.get("role"),
                content=payload.get("content"),
                chat_id=rollout_chat_id or payload.get("chat_id"),
                message_id=payload.get("id"),
                timestamp=record.get("timestamp") or payload.get("timestamp"),
            )
            if item:
                yield item
            continue

        item = message_record(
            role=record.get("role"),
            content=record.get("content") or record.get("question"),
            chat_id=record.get("chat_id") or record.get("conversation_id"),
            message_id=record.get("message_id") or record.get("id"),
            timestamp=record.get("timestamp") or record.get("created_at"),
        )
        if item:
            yield item


def classify_question(question: str) -> str:
    searchable = question.casefold()
    if any(term.casefold() in searchable for term in SYSTEM_TERMS):
        return "system"
    if any(term.casefold() in searchable for term in WIKI_TERMS):
        return "wiki"
    return "other"


def make_fingerprint(item: dict[str, Any]) -> str:
    if item.get("message_id"):
        identity = f"message-id\0{item['chat_id']}\0{item['message_id']}"
    else:
        identity = (
            f"fallback\0{item['chat_id']}\0{item['timestamp']}\0{item['question']}"
        )
    return "sha256:" + hashlib.sha256(identity.encode("utf-8")).hexdigest()


def load_fingerprints(path: Path) -> set[str]:
    if not path.exists():
        return set()
    fingerprints: set[str] = set()
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid stored JSONL at {path}:{line_number}: {exc}") from exc
            fingerprint = record.get("fingerprint")
            if fingerprint:
                fingerprints.add(str(fingerprint))
    return fingerprints


def build_new_records(
    messages: Iterable[dict[str, Any]],
    existing: set[str],
    chat_id_filter: str | None,
) -> tuple[list[dict[str, Any]], int]:
    new_records: list[dict[str, Any]] = []
    duplicate_count = 0

    for item in messages:
        if chat_id_filter and item["chat_id"] != chat_id_filter:
            continue
        fingerprint = make_fingerprint(item)
        if fingerprint in existing:
            duplicate_count += 1
            continue

        new_records.append(
            {
                "timestamp": item["timestamp"],
                "chat_id": item["chat_id"],
                "question": item["question"],
                "flag": classify_question(item["question"]),
                "message_id": item.get("message_id"),
                "fingerprint": fingerprint,
                "logged_at": utc_now(),
                "schema_version": 1,
            }
        )
        existing.add(fingerprint)

    return new_records, duplicate_count


def append_records(path: Path, records: Iterable[dict[str, Any]]) -> int:
    records = list(records)
    if not records:
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")
        handle.flush()
    return len(records)


def main() -> int:
    args = parse_args()
    try:
        input_paths = (
            [args.input]
            if args.input
            else discover_project_rollouts(args.sessions_root, args.project_root)
        )
        messages: list[dict[str, Any]] = []
        for input_path in input_paths:
            messages.extend(extract_messages(read_input(input_path)))
        existing = load_fingerprints(args.output)
        records, duplicate_count = build_new_records(messages, existing, args.chat_id)

        if args.dry_run:
            for record in records:
                print(json.dumps(record, ensure_ascii=False, indent=2))
            written = 0
        else:
            written = append_records(args.output, records)

        print(f"Conversations scanned: {len(input_paths)}", file=sys.stderr)
        print(f"User messages found: {len(messages)}", file=sys.stderr)
        print(f"Duplicates skipped: {duplicate_count}", file=sys.stderr)
        print(f"New records {'proposed' if args.dry_run else 'appended'}: {len(records)}", file=sys.stderr)
        if not args.dry_run:
            print(f"Output: {args.output}", file=sys.stderr)
        return 0
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
