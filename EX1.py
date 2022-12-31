
from IGraph import Graph
import matplotlib.pyplot as plt
import random

G = Graph()
visited = []

#G.set_from_dotFile('GraphsFiles/test.dot')
# G.set_from_dotFile('GraphsFiles/biGraph.dot')
G.set_from_dotFile('GraphsFiles/biGraph1.dot')
# G.set_from_dotFile('GraphsFiles/tree.dot')

# G.set_nodes_color(['2','4'], 'red')
# G.set_edges_color([('1','2'), ('1','4')], 'blue')
# G.set_node_color('1','r')
# G.set_edge_color(('1','2'),'g')
# G.set_edge_weight(('1','2'), 5)
G.set_random_edges_weights(0, 20)
# print (G.get_edge_weight(('1','2')))
# plt.subplot(1,2,1)
# G.draw()
# plt.subplot(1,2,2)

# print (G.get_neighbours('1'))
# print(G.get_nodes())
# print(G.get_edges('1'))
# print(G.get_edges('20'))
# print(f'neighbours of node 20 = {G.get_neighbours("20")}')



# visited = G.DFS_recursive('1')
# visited = G.DFS_recursice_visited_check('1')
# visited = G.DFS_stack('1')
# visited = G.BFS('1')
visited0 = G.find_path_DFS('B', '20')
visited1 = G.find_path_BFS('B', '20')
visited2 = G.UCS('B', '20')
print('DFS: blue', visited0)
print('BFS: red', visited1)
print('UCS: green', visited2)

plt.subplot(1,3,1)
G.set_node_color(node_list = visited0, color ='blue')
G.draw('neato')
plt.title("DFS B->20")


plt.subplot(1,3,2)
G.set_all_nodes_color()

G.set_node_color(node_list=visited1,color='red')
G.draw('neato')
plt.title("BFS B->20")

plt.subplot(1,3,3)
G.set_all_nodes_color()
G.set_node_color(node_list=visited2,color='green')
plt.title("UCS B->20")
G.draw('neato')
G.draw_edge_attributes (layout='neato')

plt.show()


