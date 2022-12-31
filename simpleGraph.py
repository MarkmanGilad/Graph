# need to install graphviz and c++
# https://pygraphviz.github.io/
# https://pygraphviz.github.io/documentation/stable/install.html

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3,4,5])

G.add_edge(1,2)
G.add_edges_from([(3,2), (1,3), (3,5), (5,4), (1,4), (2,4)])

D = nx.DiGraph()

D.add_edges_from([(3,2), (1,3), (3,5), (1,4) ])

#T = nx.balanced_tree(2, 5)

# nx.nx_agraph.write_dot(D, 'test.dot')

pos = graphviz_layout(D, prog='dot')

subax1 = plt.subplot(131)
nx.draw(G, pos, with_labels=True)

subax2 = plt.subplot(132)
nx.draw(G, with_labels=True)

subax3 = plt.subplot(133)
nx.draw(D, pos, with_labels=True)
plt.show()

class matrixGraph:
    pass

class listGraph:
    pass