const { ItemView, Plugin, Notice, MarkdownRenderer, getAllTags } = require("obsidian");

const VIEW_TYPE = "llm-wiki-graphify-view";
const NODE_COLOR = "#00FFD0";

function buildVaultGraph(app) {
  const files = app.vault.getMarkdownFiles().filter((file) =>
    file.path.startsWith("01_sources/") || file.path.startsWith("02_wiki/")
  );
  const fileByPath = new Map(files.map((file) => [file.path, file]));
  const communityNames = [...new Set(files.map((file) => file.path.includes("/") ? file.path.split("/")[0] : "Root"))].sort();
  const communityId = new Map(communityNames.map((name, index) => [name, index]));
  const metrics = new Map(files.map((file) => [file.path, { inbound: 0, outbound: 0 }]));
  const edges = [];

  Object.entries(app.metadataCache.resolvedLinks || {}).forEach(([source, targets]) => {
    if (!fileByPath.has(source)) return;
    Object.entries(targets || {}).forEach(([target, rawCount]) => {
      if (!fileByPath.has(target) || source === target) return;
      const count = Math.max(1, Number(rawCount) || 1);
      metrics.get(source).outbound += count;
      metrics.get(target).inbound += count;
      edges.push({
        from: source,
        to: target,
        label: "",
        title: `${count} resolved link${count === 1 ? "" : "s"}`,
        dashes: false,
        width: Math.min(4, 1 + Math.log2(count + 1) * 0.45),
        color: { color: NODE_COLOR, highlight: NODE_COLOR, hover: NODE_COLOR, inherit: false, opacity: 0.38 },
        confidence: "EXTRACTED"
      });
    });
  });

  const counts = new Map(communityNames.map((name) => [name, 0]));
  const nodes = files.map((file) => {
    const communityName = file.path.includes("/") ? file.path.split("/")[0] : "Root";
    const cid = communityId.get(communityName);
    const metric = metrics.get(file.path);
    const degree = metric.inbound + metric.outbound;
    // Match the size scale while keeping the same neon turquoise hue.
    const intensity = Math.min(1, Math.pow(degree, 0.75) * 1.8 / 57);
    const opacity = 0.2 + 0.8 * intensity;
    const cache = app.metadataCache.getFileCache?.(file);
    const hasAlmTag = (cache ? getAllTags(cache) || [] : [])
      .some((tag) => tag.replace(/^#/, "").toLowerCase() === "alm");
    const color = hasAlmTag
      ? `rgba(255, 230, 0, ${opacity})`
      : `rgba(0, 255, 208, ${opacity})`;
    counts.set(communityName, counts.get(communityName) + 1);
    return {
      id: file.path,
      label: file.basename,
      color: { background: color, border: color, highlight: { background: color, border: "#ffffff" } },
      size: 3 + Math.min(57, Math.pow(degree, 0.75) * 1.8),
      font: { size: 0, color: "#ffffff" },
      title: `${file.basename}\n${degree} links (${metric.outbound} out / ${metric.inbound} in)`,
      community: cid,
      community_name: communityName,
      source_file: file.path,
      file_type: "markdown",
      degree,
      inbound: metric.inbound,
      outbound: metric.outbound,
      hasAlmTag
    };
  });

  const legend = communityNames.map((name) => ({
    cid: communityId.get(name),
    color: NODE_COLOR,
    label: name,
    count: counts.get(name)
  }));
  return { nodes, edges, legend };
}

function injectVaultGraph(template, graph) {
  let html = template.replace(
    /<div id="stats">[\s\S]*?<\/div>/,
    `<div id="stats">${graph.nodes.length} nodes &middot; ${graph.edges.length} edges &middot; ${graph.legend.length} communities</div>`
  );
  html = html.replace(/const RAW_NODES = [\s\S]*?;\r?\nconst RAW_EDGES = /, `const RAW_NODES = ${JSON.stringify(graph.nodes)};\nconst RAW_EDGES = `);
  html = html.replace(/const RAW_EDGES = [\s\S]*?;\r?\nconst LEGEND = /, `const RAW_EDGES = ${JSON.stringify(graph.edges)};\nconst LEGEND = `);
  html = html.replace(/const LEGEND = [\s\S]*?;\r?\n\r?\n\/\/ HTML-escape helper/, `const LEGEND = ${JSON.stringify(graph.legend)};\n\n// HTML-escape helper`);
  html = html.replace("</body>", `<script>\nnetwork.on('doubleClick', function(params) {\n  if (!params.nodes.length) return;\n  const node = RAW_NODES.find(function(item) { return item.id === params.nodes[0]; });\n  if (node) parent.postMessage({ type: 'llm-wiki-graphify-open', path: node.source_file }, '*');\n});\n</script>\n</body>`);
  return html;
}

class GraphifyHtmlView extends ItemView {
  constructor(leaf, plugin) {
    super(leaf);
    this.plugin = plugin;
    this.frame = null;
    this.graph = null;
    this.infoPanel = null;
    this.infoContent = null;
    this.infoRequestId = 0;
    this.onMessage = (event) => this.handleMessage(event);
  }

  getViewType() { return VIEW_TYPE; }
  getDisplayText() { return "Graphify View"; }
  getIcon() { return "git-fork"; }

  async onOpen() {
    this.contentEl.empty();
    this.contentEl.addClass("llm-graphify-original-view");
    const infoPanel = this.contentEl.createEl("aside", { cls: "llm-graphify-node-info" });
    infoPanel.addClass("is-collapsed");
    this.infoPanel = infoPanel;
    infoPanel.createEl("h3", { text: "Node Info" });
    this.infoContent = infoPanel.createDiv({ cls: "llm-graphify-node-info-content" });
    this.infoContent.createEl("span", { cls: "llm-graphify-empty", text: "Click a node to inspect it" });
    window.addEventListener("message", this.onMessage);
    await this.renderGraph();
    this.registerEvent(this.app.metadataCache.on("resolved", () => this.renderGraph()));
  }

  async renderGraph() {
    const htmlPath = `${this.plugin.manifest.dir}/graph.html`;
    try {
      const template = await this.app.vault.adapter.read(htmlPath);
      this.graph = buildVaultGraph(this.app);
      const html = injectVaultGraph(template, this.graph);
      if (!this.frame) {
        this.frame = this.contentEl.createEl("iframe", {
          cls: "llm-graphify-original-frame",
          attr: { title: "Graphify knowledge graph", sandbox: "allow-scripts allow-same-origin" }
        });
      }
      this.frame.srcdoc = html;
    } catch (error) {
      this.contentEl.empty();
      this.contentEl.createEl("p", { text: `Cannot render Graphify View: ${error.message}` });
    }
  }

  async handleMessage(event) {
    if (!this.frame || event.source !== this.frame.contentWindow) return;
    if (event.data?.type === "llm-wiki-graphify-read") {
      const { path } = event.data;
      if (typeof path !== "string" || !(path.startsWith("01_sources/") || path.startsWith("02_wiki/"))) return;
      await this.renderNodeInfo(path);
      return;
    }
    if (event.data?.type === "llm-wiki-graphify-clear") {
      this.clearNodeInfo();
      return;
    }
    if (!event.data || event.data.type !== "llm-wiki-graphify-open") return;
    const file = this.app.vault.getAbstractFileByPath(event.data.path);
    if (file) await this.app.workspace.getLeaf(false).openFile(file);
  }

  clearNodeInfo() {
    this.infoRequestId += 1;
    this.infoPanel?.addClass("is-collapsed");
    if (!this.infoContent) return;
    this.infoContent.empty();
    this.infoContent.createEl("span", { cls: "llm-graphify-empty", text: "Click a node to inspect it" });
  }

  async renderNodeInfo(path) {
    if (!this.infoContent) return;
    const requestId = ++this.infoRequestId;
    this.infoPanel?.removeClass("is-collapsed");
    this.infoContent.empty();
    const node = this.graph?.nodes.find((item) => item.id === path);
    const note = this.app.vault.getAbstractFileByPath(path);
    if (!note || note.extension !== "md") {
      this.infoContent.createEl("p", { text: "Note not found" });
      return;
    }

    this.infoContent.createEl("h2", { text: node?.label || note.basename });
    const meta = this.infoContent.createDiv({ cls: "llm-graphify-node-meta" });
    meta.createDiv({ text: `Source: ${path}` });
    if (node) {
      meta.createDiv({ text: `Links: ${node.degree} (${node.outbound} out / ${node.inbound} in)` });
    }

    const noteBody = this.infoContent.createDiv({ cls: "markdown-rendered llm-graphify-note-body" });
    try {
      const content = await this.app.vault.cachedRead(note);
      if (requestId !== this.infoRequestId) return;
      await MarkdownRenderer.render(this.app, content, noteBody, path, this);
      if (requestId !== this.infoRequestId) return;
    } catch (error) {
      noteBody.empty();
      noteBody.createEl("p", { text: `Cannot render note: ${error.message}` });
    }

    const neighbors = new Set();
    for (const edge of this.graph?.edges || []) {
      if (edge.from === path) neighbors.add(edge.to);
      if (edge.to === path) neighbors.add(edge.from);
    }
    if (neighbors.size) {
      const related = this.infoContent.createDiv({ cls: "llm-graphify-related" });
      related.createEl("h3", { text: `Related nodes (${neighbors.size})` });
      for (const neighborId of neighbors) {
        const neighbor = this.graph.nodes.find((item) => item.id === neighborId);
        const button = related.createEl("button", { text: neighbor?.label || neighborId });
        button.addEventListener("click", () => {
          this.frame?.contentWindow?.postMessage({ type: "llm-wiki-graphify-focus", nodeId: neighborId }, "*");
        });
      }
    }
  }

  async onClose() {
    window.removeEventListener("message", this.onMessage);
    if (this.frame) this.frame.srcdoc = "";
    this.frame = null;
    this.graph = null;
    this.infoPanel = null;
    this.infoContent = null;
  }
}

module.exports = class GraphifyPlugin extends Plugin {
  async onload() {
    this.registerView(VIEW_TYPE, (leaf) => new GraphifyHtmlView(leaf, this));
    this.addRibbonIcon("git-fork", "Open Graphify View", () => this.activateView());
    this.addCommand({ id: "open-graphify-view", name: "Open Graphify View", callback: () => this.activateView() });
  }
  async onunload() { this.app.workspace.detachLeavesOfType(VIEW_TYPE); }
  async activateView() {
    let leaf = this.app.workspace.getLeavesOfType(VIEW_TYPE)[0];
    if (!leaf) {
      leaf = this.app.workspace.getLeaf("tab");
      await leaf.setViewState({ type: VIEW_TYPE, active: true });
    }
    this.app.workspace.revealLeaf(leaf);
    new Notice("Graphify View rebuilt from the current vault");
  }
};

module.exports._test = { VIEW_TYPE, buildVaultGraph, injectVaultGraph, GraphifyHtmlView };
