# LLM Wiki Graphify View

Obsidian view rebuilt from the exact `graphify-out/graph.html` interface at
`https://github.com/hieunt795/llm-wiki/tree/master/graphify-out`.

## Use

1. Reload Obsidian or disable/re-enable **LLM Wiki Graphify View** in Community plugins.
2. Click the graph/fork ribbon icon, or run **Open Graphify View** from the command palette.

The original HTML supplies the layout and interactions. At runtime the plugin replaces its
embedded nodes, edges, communities, and statistics with data from the current vault. Node size
uses total resolved wikilinks (`outbound + inbound`), and double-clicking opens the note in Obsidian.

The original HTML loads `vis-network` from a CDN, so the view requires network access.
