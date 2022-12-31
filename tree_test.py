from Tree import Tree
from IGraph import IGraph
import matplotlib.pyplot as plt

G = IGraph()

# G.set_from_dotFile('GraphsFiles/tree.dot')
# G.draw()
# path = G.find_path_DFS ('1', '20')
# G.set_node_color(color='red', node_list=path)
T = Tree('GraphsFiles/BinaryTree.dot')
# print(T.get_neighbours('10'))
# print (T.hasSon('7'))
# print (T.LeftSon('7'))
# print (T.RightSon('7'))

plt.ion()

T.DFS(T.root)
print()
print (T.path)
print("Max Leaf: ", T.DFS_FindMaxLeaf(T.root))
print("Depth", T.DFS_depth(T.root, 0))
print("Count leafs", T.DFS_count_leafs(T.root))
print("sum Of leafs", T.DFS_sum_of_leafs(T.root))
T.DFS_Path('1', '15')

T.draw()
T.draw_node_attributes('value')
# T.draw_path()
plt.pause(1)
T.Draw_path_dynamically()
plt.ioff()
plt.show()