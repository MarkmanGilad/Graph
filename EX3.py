from IGraph import Graph
import matplotlib.pyplot as plt
import random

plt.ion()


# build weighted graph
G3 = Graph()
G3.set_from_dotFile('GraphsFiles/biGraph1.dot')
edges = G3.get_edges()
dict_values = {}
for e in edges:
    dict_values[e] = {"weight" :random.randint(0 , 20)}
G3.set_edge_weight(dict_values=dict_values)


# search BFS


# plt.subplot(2,2,4)
plt.title("find UCS 20 -> A")
plt.box(False)
#G3.draw('neato')

G3.draw_nodes(layout='neato')
G3.draw_edges(layout='neato')
plt.pause(0.5)
G3.draw_labels(layout='neato')
plt.pause(0.5)
G3.draw_edge_attributes('weight', layout='neato')
plt.pause(0.5)
path = G3.UCS('20', 'A')
print("find UCS", path)
G3.set_node_color(node_list=path, color='red')
G3.save_to_dotFile('GraphsFiles/G3.dot')
#G3.draw('neato')
G3.draw_nodes(layout='neato')
print(G3.air_distance('20', 'A',layout='neato'))
#plt.show()
plt.pause(60)