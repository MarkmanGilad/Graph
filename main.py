
from Graph import myGraph
import matplotlib.pyplot as plt
import random

G = myGraph()
visited = []

#G.set_from_dotFile('GraphsFiles/test.dot')
G.set_from_dotFile('GraphsFiles/biGraph.dot')
# G.set_from_dotFile('GraphsFiles/tree.dot')

#G.set_nodes_color(['2','4'], 'red')
#G.set_edges_color([('1','2'), ('1','4')], 'blue')
# G.set_node_color('1','r')
# G.set_edge_color(('1','2'),'g')
#G.set_edge_weight(('1','2'), 5)
#print (G.get_edge_weight(('1','2')))
#plt.subplot(1,2,1)
#G.draw()
#plt.subplot(1,2,2)

#print (G.get_neighbours('1'))
#print(G.get_nodes())
#print(G.get_edges('1'))
#print(G.get_edges('20'))
#print(f'neighbours of node 20 = {G.get_neighbours("20")}')
plt.title("Graph")


# visited = G.DFS_recursive('1')
# visited = G.DFS_recursice_visited_check('1')
# visited = G.DFS_stack('1')
# visited = G.BFS('1')
# visited = G.find_path_DFS('1', '20')
# visited = G.find_path_BFS('B', '20')
nodesList = G.get_nodes()
randomlist = random.sample(range(0, 20), len(nodesList))
G.set_nodes_attributes(G.get_nodes(), 'weight', randomlist)


print(visited)
G.set_nodes_color(visited, 'g')
# draw: 'dot', 'twopi', 'fdp', 'sfdp', 'circo', 'neato'
G.draw('neato')
plt.show()


