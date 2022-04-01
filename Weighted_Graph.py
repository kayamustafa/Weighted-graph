import networkx as nx
import matplotlib.pyplot as plt

# Kısa yolları yazdırmak için fonksiyon
def dijkstra_yazdir():
    print("4 ile 0 arası: ", end='')
    try:
        sp0 = nx.dijkstra_path(G1, 4, 0)
        print(sp0)
    except nx.NetworkXNoPath:
        print("Böyle bir yol yok")
    print("4 ile 1 arası: ", end='')
    try:
        sp1 = nx.dijkstra_path(G1, 4, 1)
        print(sp1)
    except nx.NetworkXNoPath:
        print("Böyle bir yol yok")
    print("4 ile 2 arası: ", end='')
    try:
        sp2 = nx.dijkstra_path(G1, 4, 2)
        print(sp2)
    except nx.NetworkXNoPath:
        print("Böyle bir yol yok")
    print("4 ile 3 arası: ", end='')
    try:
        sp3 = nx.dijkstra_path(G1, 4, 3)
        print(sp3)
    except nx.NetworkXNoPath:
        print("Böyle bir yol yok")


G1 = nx.DiGraph()

G1.add_node(0)
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)

G1.add_edge(0, 1, weight=5)
G1.add_edge(0, 2, weight=3)
G1.add_edge(0, 4, weight=2)
G1.add_edge(1, 2, weight=2)
G1.add_edge(1, 3, weight=6)
G1.add_edge(2, 1, weight=1)
G1.add_edge(2, 3, weight=2)
G1.add_edge(4, 1, weight=6)
G1.add_edge(4, 2, weight=10)
G1.add_edge(4, 3, weight=4)

G1.nodes[0]['pos'] = (3,1)
G1.nodes[1]['pos'] = (5,0)
G1.nodes[2]['pos'] = (4,-1)
G1.nodes[3]['pos'] = (2,-1)
G1.nodes[4]['pos'] = (1,0)

pos=nx.get_node_attributes(G1,'pos')
nx.draw_networkx(G1, pos)
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G1.edges(data=True)])
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)
plt.axis('off')
plt.show()

dijkstra_yazdir()

print("\nNode 3 silindikten sonra:")

# Node 3 silindikten sonra
G1.remove_node(3)
pos=nx.get_node_attributes(G1,'pos')
nx.draw_networkx(G1, pos)
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G1.edges(data=True)])
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)
plt.axis('off')
plt.show()

dijkstra_yazdir()

G1.clear()


