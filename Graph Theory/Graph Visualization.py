import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edge("a", "b", weight = 0.6)
G.add_edge("a", "c", weight = 0.2)
G.add_edge("c", "d", weight = 0.1)
G.add_edge("c", "e", weight = 0.7)
G.add_edge("c", "f", weight = 0.9)
G.add_edge("a", "d", weight = 0.3)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed = 7)
nx.draw_networkx_nodes(G, pos, alpha = 0.7, node_size = 1000)
nx.draw_networkx_edges(G, pos, edgelist = elarge, width = 5, alpha = 0.2, edge_color = "r")
nx.draw_networkx_edges(G, pos, edgelist = esmall, width = 5, alpha = 0.5, edge_color = "b", style = "dashed")

nx.draw_networkx_labels(G, pos, font_size = 20, font_family = "sans-serif")
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
ax = plt.gca()
ax.margins(0.08)
plt.tight_layout()

plt.axis("off")
plt.show()