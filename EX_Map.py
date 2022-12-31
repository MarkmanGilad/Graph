
from IGraph import Graph, IGraph
import matplotlib.pyplot as plt
import random

layout = "neato"
start = 'M'
goal = 'J'


plt.ion()

G = Graph()
G.set_from_dotFile('GraphsFiles/map.dot')


edges = G.get_edges()
for edge in edges:
    distance = round(G.air_distance(edge[0], edge[1]) * random.uniform(1, 1))
    G.set_edge_weight(edge, distance)
G.save_to_dotFile('GraphsFiles/mapWithDistance.dot')
plt.subplot(1,2,1)
G.draw(layout)
G.draw_edge_attributes(layout= layout)
print(G.air_distance(start, goal))
plt.title("MAP")
plt.show()
plt.pause(1)

# plt.clf()

path = G.UCS(start, goal)
print (f'UCS: {start} -> {goal}',path)
print(G.get_node_attribute(goal, 'distance'))
G.set_node_color(node_list=path, color='green')
G.draw(layout, node_labels=True)
G.draw_edge_attributes(layout=layout)
plt.show()
plt.pause(3)

##################### aStar #########################
plt.subplot(1,2,2)
G1 = Graph()
G1.set_from_dotFile('GraphsFiles/mapWithDistance.dot')
path = G1.aStar(start, goal)
print (f'aStar: {start} -> {goal}',path)
print(G1.get_node_attribute(goal, 'cost'))
G1.set_node_color(node_list=path, color='green')
G1.draw(layout, node_labels=True)
G1.draw_edge_attributes(layout=layout)


plt.pause(330)

