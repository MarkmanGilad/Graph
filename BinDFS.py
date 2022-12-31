from Tree import Tree
import matplotlib.pyplot as plt

T = Tree('GraphsFiles/Tree.dot')
T.DFS(T.root)
print(T.path)
T.draw()
plt.show()
