# need to install graphviz and c++
# https://pygraphviz.github.io/
# https://pygraphviz.github.io/documentation/stable/install.html

import networkx as nx
# from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

D = nx.DiGraph()

D.add_edges_from([(1,3), (3, 2), (3,5), (1,4)])
coord = {1: [7,0], 3: [6, -1], 2: [4, -2], 5: [7, -2], 4: [9, -2]}
# write_dot(D, 'test.dot')
nx.draw(D, pos = coord, with_labels=True)
plt.show()

