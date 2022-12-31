from logging import root
from IGraph import Graph
import matplotlib.pyplot as plt
import random

# plt.ion()

G = Graph()
G.set_from_dotFile('GraphsFiles/tree.dot')
G.set_node_attribute('1', 'node_shape', 'v')
G.set_node_attribute('2', 'node_shape', '^')
# G.set_node_color ('1', 'lightblue')
# G.set_node_attribute('2', 'color', 'red')
plt.subplot(1,2,1)

print(G.get_neighbours('14'))
G.add_depth('1')
G.draw(node_labels = True, layout='dot', nodes_shape=True)
G.draw_node_attributes (attr_name='depth', x_bias = 15, y_bias = 0, font_size = 8, font_color = 'r', layout='dot')
# plt.box(False)
plt.subplot(1,2,2)
G.set_minmax_shape(start='max')
G.draw(nodes_shape=True, node_labels = False)
G.draw_node_attributes (attr_name='Q', x_bias = 15, y_bias = 0, font_size = 8, font_color = 'r', layout='dot')
G.save_to_dotFile('GraphsFiles/tree1.dot')
plt.show()