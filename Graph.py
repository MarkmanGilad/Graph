from IGraph import IGraph

class myGraph (IGraph):

    def __init_subclass__():
        return super().__init__()

    def DFS_recursive (self, node):
            # only tree - directed graph - no loops
            self.clear_path()
            self.DFS_recursive_1(node)
            return self.path
        
    def DFS_recursive_1 (self, node):
        self.path.append(node) 
        if len(self.get_neighbours(node)) == 0: # not needed. part of the loop 
            return
        for n in self.get_neighbours(node):
            self.DFS_recursive_1(n)

    def DFS_recursice_visited_check (self, node):
        visited = []
        self.DFS_recursice_visited_check_1(node, visited)
        return visited

    def DFS_recursice_visited_check_1 (self, node, visited):
        visited.append(node)
        for n in self.get_neighbours(node):
            if not n in visited:
                self.DFS_recursice_visited_check_1 (n, visited)

    def DFS_stack (self, node):
        # include visited check - avoid loops
        visited = []
        stack = [node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack = list(reversed(self.get_neighbours(node))) + stack # you don't need the reverse
                #neighbours = list(reversed(self.get_neighbours(node)))  
                #for n in neighbours:
                #    stack.append(n)
                    
        return visited

    def BFS (self, node):
        visited = []
        frontier = [node]
        while frontier:
            node = frontier.pop(0)
            if node not in visited:
                visited.append(node)
                #frontier.extend(self.get_neighbours(node))
                frontier += self.get_neighbours(node)
                    
        return visited

    def find_path_DFS (self, start, goal):
        self.clear_path()
        self.find_path_DFS_1 (start, goal, [], [])
        return self.path

    def find_path_DFS_1 (self, start, goal, visited, path):
        # tree only
        path.append(start)
        visited.append(start)
        if start == goal:
            self.path = path.copy()

        for n in self.get_neighbours(start):
            if n not in visited:
                self.find_path_DFS_1(n, goal, visited, path)
                path.pop()

    def find_path_BFS (self, start, goal):
        visited = []
        frontier = [start]
        self.G.nodes[start]["path"] = [start]
        while frontier:
            node = frontier.pop(0)
            if node == goal:
                return self.get_node_attribute(goal, "path")
            if node not in visited:
                visited.append(node)
                neighbours = self.get_neighbours(node) 
                for n in neighbours:
                    if n not in visited and n not in frontier:
                        frontier.append(n)
                        path = self.get_node_attribute(node, "path")
                        path.append(n)
                        self.G.nodes[n]["path"] = path
        return self.get_node_attribute(goal, "path")

    def UCS (self, start, goal):

        visited = []
        frontier = {start : 0}
        self.set_node_attribute(start, "path", [start])
        while frontier:
            node = min(frontier, key=frontier.get)
            distance = frontier[node]
            frontier.pop(node)
            if node == goal:
                return self.get_node_attribute(goal, "path")
            if node not in visited:
                visited.append(node)
                neighbours = self.get_neighbours(node) 
                for n in neighbours:
                    if n not in visited:
                        new_distance = distance + self.get_edge_weight((node, n))
                        if n not in frontier:
                            frontier[n] = new_distance
                            path = self.get_node_attribute(node, "path")
                            path.append(n)
                            self.set_node_attribute(n,"path", path)
                            self.set_node_attribute(n, "distance", new_distance)

                        else:
                            if new_distance < frontier[n]:
                                frontier[n] = new_distance
                                path = self.get_node_attribute(node, "path")
                                path.append(n)
                                self.set_node_attribute(n,"path", path)
                                self.set_node_attribute(n, "distance", new_distance)
                        
        return self.get_node_attribute(goal, "path")

    def Bellman_ford (self, start, goal):
        pass


