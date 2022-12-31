from IGraph import IGraph
import matplotlib.pyplot as plt

class Tree (IGraph):
    
    def __init__(self, path = None):
        super().__init__()
        if path:
            self.set_from_dotFile(path)
            if not self.is_tree():
                raise Exception (f'The Graph {path} is not a tree')
            self.root = self.get_nodes()[0]

    def hasSon (self, node):
        return bool(self.get_neighbours(node))

    def isLeaf(self, node):
        return not self.hasSon(node)

    def leftSon (self, node):
        if len(self.get_neighbours(node)) > 0:
            return self.get_neighbours(node)[0]
        return None

    def rightSon (self, node):
        if len(self.get_neighbours(node)) > 1:
            return self.get_neighbours(node)[1]
        return None

    def draw_path (self, color = 'red'):
        self.set_node_color(node_list=self.path, color=color)
        self.draw_nodes()
        
    def Draw_path_dynamically(self, color='red', plt=plt):
        for node in self.path:
            self.set_node_color(node=node, color=color)
            self.draw_nodes()
            plt.pause(0.5)
            self.set_node_color(node=node, color='lightBlue')
        self.draw_nodes()

    def DFS (self, node):
        pass
    
    def DFS_FindMaxLeaf(self, node):
        pass
        
    def DFS_depth (self, node, d):
        pass

    def DFS_count_leafs(self, node):
        pass

    def DFS_sum_of_leafs(self, node):
        pass
    
    def DFS_Path (self, start, goal, path=[]):
        pass
        


