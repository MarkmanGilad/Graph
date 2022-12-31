from IGraph import IGraph


class Graph (IGraph):

    def __init__(self):
        return super().__init__()

    def DFS_recursive (self, node):
            # only tree - directed graph - no loops
            self.clear_path()
            self.__DFS_recursive(node)
            return self.path
        
    def __DFS_recursive (self, node):
        self.path.append(node) 
        if len(self.get_neighbours(node)) == 0: # not needed. part of the loop 
            return
        for n in self.get_neighbours(node):
            self.DFS_recursive_1(n)

    def DFS_recursice_visited_check (self, node):
        visited = []
        self.__DFS_recursice_visited_check(node, visited)
        return visited

    def __DFS_recursice_visited_check (self, node, visited):
        visited.append(node)
        for n in self.get_neighbours(node):
            if not n in visited:
                self.__DFS_recursice_visited_check (n, visited)

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
        self.__find_path_DFS (start, goal, [], [])
        return self.path

    def __find_path_DFS (self, start, goal, visited, path):
        path.append(start)
        visited.append(start)
        if start == goal:
            self.path = path.copy()

        for n in self.get_neighbours(start):
            if n not in visited:
                self.__find_path_DFS(n, goal, visited, path)
                path.pop()

    def find_path_BFS (self, start, goal):
        visited = []
        frontier = [start]
        #self.G.nodes[start]["path"] = [start]
        self.set_node_attribute(start, 'path', [start])
        while frontier:
            node = frontier.pop(0)
            if node == goal:
                return self.get_node_attribute(node=goal,name= "path")
            if node not in visited:
                visited.append(node)
                neighbours = self.get_neighbours(node) 
                for n in neighbours:
                    if n not in visited and n not in frontier:
                        frontier.append(n)
                        path = self.get_node_attribute(node=node, name="path")
                        path.append(n)
                        #self.G.nodes[n]["path"] = path
                        self.set_node_attribute(n, 'path', path)
        return self.get_node_attribute(node=goal, name="path")

    def UCS (self, start, goal):
        counter = 0
        visited = []
        frontier = {start : 0}
        self.set_node_attribute(node=start, name="path", value=[start])
        self.set_node_attribute(node=start, name="distance", value=0)
        while frontier:
            node = min(frontier, key=frontier.get)
            distance = frontier[node]
            frontier.pop(node)
            counter +=1
            print(counter, end=',')
            if node == goal:
                return self.get_node_attribute(node=goal, name="path")
            #if node not in visited:
            visited.append(node)
            neighbours = self.get_neighbours(node) 
            for n in neighbours:
                if n not in visited:
                    new_distance = distance + self.get_edge_weight((node, n))
                    if n not in frontier:
                        frontier[n] = new_distance
                        path = self.get_node_attribute(node=node, name="path")
                        path.append(n)
                        self.set_node_attribute(n,"path", path)
                        self.set_node_attribute(n, "distance", new_distance)
                    else:
                        if new_distance < frontier[n]:
                            frontier[n] = new_distance
                            path = self.get_node_attribute(node=node, name="path")
                            path.append(n)
                            self.set_node_attribute(n,"path", path)
                            self.set_node_attribute(n, "distance", new_distance)
                    
        return self.get_node_attribute(node=goal, name= "path")

    def Bellman_ford (self, start, goal):
        pass

    def find_min_node(self, attribute = 'Q'):
        # use DFS with recurtion
        pass

    def find_max_node(self, attribute = 'Q'):
        # use DFS with stack
        pass
    
    def find_min_leaf(self, start):
        # use DFS with recurtion
        pass

    def find_max_leaf(self, start):
        # use DFS with stack
        pass

    def aStar(self, start, goal, heuristic=None):
        counter = 0
        if heuristic == None:
            heuristic = self.air_distance
        
        visited = []
        self.set_node_attribute(start, 'path', [])
        self.set_node_attribute(start, 'cost', 0)
        frontier = {start : 0} # value = cost + h()

        while frontier:
            current = min(frontier, key=frontier.get)
            path = self.get_node_attribute(node = current, name ='path')
            cost = self.get_node_attribute(node = current, name = 'cost')
            frontier.pop(current)
            if current == goal:
                return self.get_node_attribute(node = goal, name ="path") + [goal]
            counter +=1
            print(counter, end=',')
            visited.append(current)
            neighbours = self.get_neighbours(current)
            for neighbour in neighbours:
                if neighbour not in visited:
                    new_cost = cost  + int(self.get_edge_weight((current, neighbour)))
                    if neighbour not in frontier:
                        self.set_node_attribute(neighbour, 'path', path + [current])
                        self.set_node_attribute(neighbour, 'cost', new_cost)                            
                        frontier[neighbour] = new_cost + heuristic(neighbour, goal)
                    else:
                        if new_cost < self.get_node_attribute(node = neighbour, name ='cost'):
                            self.set_node_attribute(neighbour, 'cost', new_cost)
                            frontier[neighbour] = new_cost + heuristic(neighbour, goal)
                            self.set_node_attribute(neighbour, 'path', path + [current])
                            
                        
        return [] #self.get_node_attribute(goal, "path")


################### minMax ##########################################

    def minMax (self, start, maxDepth = None):
        pass

    def minMax_alpha_beta(self, start, maxDepth = None):
        pass
