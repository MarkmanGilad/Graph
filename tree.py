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
        if not node:   
            return
        self.path.append(node)
        self.DFS (self.leftSon(node))
        self.DFS (self.rightSon(node))

    
    def DFS_FindMaxLeaf(self, node):
        
        if not self.hasSon(node):
            return int(self.get_node_attribute(name='value', node=node))
        left = right = -100
        if self.leftSon(node):
            left = self.DFS_FindMaxLeaf (self.leftSon(node))
        if self.rightSon(node):
            right = self.DFS_FindMaxLeaf (self.rightSon(node))
        return max(left, right) 
        
    def DFS_depth (self, node, d):
        if self.isLeaf(node):
            return d
        left = right = 0
        if self.leftSon(node):
            left = self.DFS_depth(self.leftSon(node), d+1)
        if self.rightSon(node):
            right = self.DFS_depth(self.rightSon(node), d+1)
        return max(left, right)

    def DFS_count_leafs(self, node):
        if  self.isLeaf(node):
            return 1
        left = right = 0
        if self.leftSon(node):
            left = self.DFS_count_leafs(self.leftSon(node))
        if self.rightSon(node):
            right = self.DFS_count_leafs(self.rightSon(node))
        return left+ right

    def DFS_sum_of_leafs(self, node):
        if  self.isLeaf(node):
            return int(self.get_node_attribute(name='value', node=node))
        left = right = 0
        if self.leftSon(node):
            left = self.DFS_sum_of_leafs(self.leftSon(node))
        if self.rightSon(node):
            right = self.DFS_sum_of_leafs(self.rightSon(node))
        return left+ right

    def DFS_Path (self, start, goal, path=[]):
        path.append(start)
        if not start:
            return
        if start == goal:
            self.path=path.copy()
            return

        self.DFS_Path (self.leftSon(start), goal, path)
        path.pop()
        self.DFS_Path (self.rightSon(start), goal, path)
        path.pop()

    def DFS_Path2 (self, start, goal, path=[]):


        
        if start == goal:
            path.append(start)
            self.path=path.copy()           
        if self.isLeaf(start):
            path.append(start)
            return
        path.append(start)
        if self.leftSon(start):
            self.DFS_Path2(self.leftSon(start), goal, path)
            path.pop()
        if self.rightSon(start):
            self.DFS_Path2(self.rightSon(start), goal, path)
            path.pop()