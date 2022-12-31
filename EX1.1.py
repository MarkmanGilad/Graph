from IGraph import IGraph
import matplotlib.pyplot as plt

G = IGraph()
G.set_from_dotFile('GraphsFiles/simple.dot')
G.draw(layout='dot')
plt.show()

# print (G.get_nodes())
# print (G.get_edges())

# G1 = IGraph()
# G2 = IGraph()
# visited = []

# G.set_from_dotFile('GraphsFiles/test.dot')
# G.set_from_dotFile('GraphsFiles/biGraph.dot')
# G.set_from_dotFile('GraphsFiles/biGraph1.dot')
# G.set_from_dotFile('GraphsFiles/tree.dot')
# G.set_from_dotFile('GraphsFiles/G3.dot')
# G1.set_from_dotFile('GraphsFiles/simple.dot')
# G2.set_from_dotFile('GraphsFiles/simpleDirected.dot')
# G.set_from_dotFile('GraphsFiles/treeUndirected.dot')
# G.set_from_dotFile('GraphsFiles/BinaryTree.dot')

# G.set_all_nodes_color(color='yellow')
# G.set_random_edges_weights(1, 10)

# G.set_node_color('1', 'red')
# G.set_node_color(color_dic={'2':'yellow', '3': 'blue'})
# list = ['1', '2', '3']
# G.set_node_color(color='red', node_list=list)

# G.draw_nodes()
# G.draw_edges()
# G.draw_labels()

# G.draw_edge_attributes()
# G.draw_node_attributes(attr_name='color')

# layout = 'dot', 'twopi', 'fdp', 'sfdp', 'circo', 'neato'

# plt.subplot(2, 2, 1)
# G.draw(layout='neato')
# plt.subplot(2, 2, 2)
# G.draw(layout='fdp')
# plt.subplot(2, 2, 3)
# G.draw(layout='dot')
# plt.subplot(2, 2, 4)
# G.draw(layout='circo')

# plt.subplot(1,2,1)
# plt.title("Undirected graph")
# G1.draw(layout='neato')
# plt.subplot(1,2,2)
# plt.title("Directed graph")
# G2.draw(layout='neato')

plt.show()