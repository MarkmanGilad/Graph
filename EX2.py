
from IGraph import Graph
import matplotlib.pyplot as plt
import random

plt.ion()
G1 = Graph()
G1.set_from_dotFile('GraphsFiles/biGraph.dot')
plt.subplot(2,2,1)

plt.title("find DFS 1 -> 20")
G1.draw()

plt.pause(0.5)

path = G1.find_path_DFS ('1', '20')
print("find DFS", path)
G1.set_node_color(node_list= path, color='red')
G1.draw()
plt.pause(0.5)

G2 = Graph()
G2.set_from_dotFile('GraphsFiles/biGraph.dot')
plt.subplot(2,2,2)
plt.title("find BFS 1-> 20")
G2.draw()
plt.pause(0.5)

path = G2.find_path_BFS ('1', '20')
print("find BFS", path)
G2.set_node_color(node_list=path,color='green')
G2.draw()

plt.pause(0.5)

# build weighted graph
G3 = Graph()
G3.set_from_dotFile('GraphsFiles/biGraph1.dot')

edges = G3.get_edges()
# print(edges)
dict_values = {}
for e in edges:
    dict_values[e] = {"weight" :random.randint(0 , 10)}

G3.set_edge_weight(dict_values=dict_values)

# search UCS
plt.subplot(2,2,3)
plt.title("UCS 20 -> A")
G3.draw(layout='neato', node_labels=True)
plt.pause(0.5)
G3.draw_node_attributes('distance', layout='neato')
plt.pause(0.5)
G3.draw_edge_attributes('weight', layout='neato')
plt.pause(1)
path = G3.UCS('20', 'A')
print ('UCS',path)
print(G3.get_node_attribute(node = 'A', name ='distance'))
G3.set_node_color(node_list=path, color='green')
G3.draw('neato', node_labels=True)

# search BFS
plt.pause(0.5)
G3.set_all_nodes_color('lightgrey')
plt.subplot(2,2,4)
plt.title("find BFS 20 -> A")
G3.draw('neato')
# G3.draw_nodes(layout='neato')
# G3.draw_labels(layout='neato')
plt.pause(0.5)
G3.draw_edge_attributes('weight', layout='neato')
plt.pause(0.5)
path = G3.find_path_BFS ('20', 'A')
print("find BFS", path)
G3.set_node_color(node_list=path, color='red')
G3.save_to_dotFile('GraphsFiles/G3.dot')
#G3.draw('neato')
G3.draw_nodes(layout='neato')
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()


# plt.pause(60)
plt.ioff()
plt.show()