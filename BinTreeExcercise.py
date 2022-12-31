from Tree import Tree
import matplotlib.pyplot as plt

T = Tree('GraphsFiles/Tree.dot')

T.set_node_color(color='lightBlue')

# leaf_value = {'H' :{'leaf_value': 5}, 
#             'I' :{'leaf_value': 8},
#             'J' :{'leaf_value': 15},
#             'K' :{'leaf_value': 25},
#             'L' :{'leaf_value': 12},
#             'M' :{'leaf_value': 7},
#             'N' :{'leaf_value': 43},
#             'O' :{'leaf_value': 15}  }
# T.set_node_attribute(values_dict=leaf_value)
# T.draw_node_attributes(attr_name='leaf_value')
# T.path = ['H', 'I', 'J', 'K', 'L', 'M', 'N','O']
# T.draw_path()
# T.draw()
# plt.show()

T.DFS(T.root)
print(T.path)
T.draw()
plt.pause(1)
T.Draw_path_dynamically()
plt.show()

