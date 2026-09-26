const assert = require("assert");
const fs = require("fs");
const path = require("path");
const Module = require("module");
const originalLoad = Module._load;
class ItemView {}
class Plugin {}
class Notice {}
class MarkdownRenderer {}
function getAllTags(cache) { return (cache.tags || []).map((item) => item.tag); }
Module._load = function patched(request, parent, isMain) {
  if (request === "obsidian") return { ItemView, Plugin, Notice, MarkdownRenderer, getAllTags };
  return originalLoad.call(this, request, parent, isMain);
};
const { buildVaultGraph, injectVaultGraph } = require("./main.js")._test;
const a = { path: "02_wiki/a.md", basename: "a" };
const b = { path: "02_wiki/b.md", basename: "b" };
const c = { path: "01_sources/nested/c.md", basename: "c" };
const excluded = { path: "03_state/state.md", basename: "state" };
const lookalike = { path: "02_wiki_backup/old.md", basename: "old" };
const app = {
  vault: { getMarkdownFiles: () => [a, b, c, excluded, lookalike] },
  metadataCache: { getFileCache: (file) => file === c ? { tags: [{ tag: "#ALM" }] } : { tags: [] }, resolvedLinks: {
    "02_wiki/a.md": { "02_wiki/b.md": 3, "03_state/state.md": 10, "02_wiki_backup/old.md": 4 },
    "02_wiki/b.md": { "02_wiki/a.md": 2 },
    "03_state/state.md": { "02_wiki/a.md": 20 }
  } }
};
const graph = buildVaultGraph(app);
assert.strictEqual(graph.nodes.length, 3);
assert.strictEqual(graph.edges.length, 2);
assert.strictEqual(graph.legend.length, 2);
assert.ok(!graph.nodes.some((n) => n.id === excluded.path || n.id === lookalike.path));
assert.ok(graph.nodes.find((n) => n.id === c.path).color.background.startsWith("rgba(255, 230, 0,"));
assert.strictEqual(graph.nodes.find((n) => n.id === c.path).hasAlmTag, true);
assert.strictEqual(graph.nodes.find((n) => n.id === a.path).degree, 5);
assert.strictEqual(graph.nodes.find((n) => n.id === a.path).outbound, 3);
assert.strictEqual(graph.nodes.find((n) => n.id === a.path).inbound, 2);
assert.ok(graph.nodes.find((n) => n.id === a.path).size > graph.nodes.find((n) => n.id === c.path).size);
const template = fs.readFileSync(path.join(__dirname, "graph.html"), "utf8");
const html = injectVaultGraph(template, graph);
assert.ok(html.includes("3 nodes &middot; 2 edges &middot; 2 communities"));
assert.ok(html.includes('"source_file":"02_wiki/a.md"'));
assert.ok(html.includes("llm-wiki-graphify-open"));
assert.ok(!html.includes("2343 nodes &middot; 6140 edges"));
console.log("Dynamic Graphify Obsidian tests passed");
