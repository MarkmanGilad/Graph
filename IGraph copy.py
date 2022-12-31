# need to install graphviz and c++
# https://pygraphviz.github.io/
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# https://pygraphviz.github.io/documentation/stable/install.html
# pip install --global-option=build_ext --global-option="-IC:\Program Files\Graphviz\include" --global-option="-LC:\Program Files\Graphviz\lib" pygraphviz
# pip install networkx[default]
# pip install typing-extensions - not sure

# layout = 'dot', 'twopi', 'fdp', 'sfdp', 'circo', 'neato'

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import os
import copy
import random

NODE_COLOR = 'lightgrey'
EDGE_COLOR = 'black'
LINE_WIDTH = 0.5

class IGraph:

    def __init__(self):
        self.G = None
        self.pos = None
        self.node_color_map = []
        self.edge_color_map = []
        self.edgecolors = 'blue'
        self.options = {
            "node_color" : self.node_color_map,
            "edge_color" : self.edge_color_map,
            "width" : LINE_WIDTH,
            "with_labels" : True
        }
        self.path = []
        
    def set_from_dotFile (self, path):
        dir = os.path.dirname(__file__)
        full_path = os.path.join(dir, path)
        self.G = nx.nx_agraph.read_dot(full_path)
        self.__set_node_color_map_by_attributes()
        self.__set_edge_color_map_by_attributes()
    
    def save_to_dotFile (self, path):
        dir = os.path.dirname(__file__)
        full_path = os.path.join(dir, path)
        nx.nx_agraph.write_dot(self.G, full_path)

####################### Draw   #####################

    def draw(self, layout='dot', node_labels = True, root=None, nodes_shape=False, shape='o'):
        if not nodes_shape:
            self.__draw_without_shape(layout=layout, node_labels=node_labels, root=root)
        elif self.is_node_attribute('node_shape'):
            self.draw_nodes_by_shape_attribute(layout=layout, root=root)
            self.draw_edges(layout=layout)
            if node_labels:
                self.draw_labels(layout=layout)
        else:
            self.draw_nodes(layout=layout,shape=shape, root=root)
            self.draw_edges(layout=layout)
            if node_labels:
                self.draw_labels(layout=layout)

    def __draw_without_shape (self, layout='dot', node_labels = True, root=None):
        self.options["with_labels"] = node_labels  # print nodes lables = keys
        pos = graphviz_layout(self.G, prog=layout, root=root)
        nx.draw(self.G, pos,**self.options)
     
    def draw_nodes (self, layout='dot', shape='o', root=None):
        pos = graphviz_layout(self.G, prog=layout, root=root)
        nx.draw_networkx_nodes(self.G, pos, node_color = self.node_color_map, node_shape = shape)

    def draw_nodes_by_shape_attribute(self, layout='dot', root=None):
        all_nodes = self.get_nodes()
        node_shapes = set(list(self.get_node_attribute(name='node_shape').values()))
        for shape in node_shapes:
            pos = graphviz_layout(self.G, prog=layout, root=root)
            node_list = [node for node in all_nodes if self.get_node_attribute(node=node, name='node_shape') == shape]   
            color_map = self.get_color_map_of_nodeList(nodeList=node_list)
            nx.draw_networkx_nodes(self.G, pos, node_color = color_map, nodelist=node_list, node_shape = shape)

    def draw_labels (self, layout='dot', font_size = 10, font_color = 'black', root=None):
        pos = graphviz_layout(self.G, prog=layout, root=root)
        nx.draw_networkx_labels(self.G, pos, font_color=font_color, font_size=font_size)

    def draw_node_attributes (self, attr_name='distance', x_bias = 0, y_bias = 20, font_size = 8, font_color = 'blue', layout='dot', root=None):
        labels = nx.get_node_attributes(self.G, attr_name)
        pos = graphviz_layout(self.G, prog=layout, root=root)
        attr_pos = {}
        for node, coords in pos.items():
            attr_pos[node] = (coords[0] + x_bias, coords[1] + y_bias)
        nx.draw_networkx_labels(self.G,attr_pos,labels=labels, font_size=font_size, font_color=font_color)

    def draw_edges(self, layout='dot', root=None):
        pos = graphviz_layout(self.G, prog=layout, root=root)
        nx.draw_networkx_edges(self.G, pos = pos, edge_color = self.edge_color_map, width = LINE_WIDTH)

    def draw_edge_attributes (self, attr_name='weight', layout='dot', root=None):
        e_labels = nx.get_edge_attributes(self.G, attr_name)
        pos = graphviz_layout(self.G, prog=layout, root=root)
        nx.draw_networkx_edge_labels(self.G,pos,edge_labels=e_labels)

#################### Nodes & Edges ####################

    def get_nodes (self):
        return list(self.G.nodes)

    def set_node (self, node):
        self.G.add_node(node)

    def set_edge (self, edge):  # edge = (5, 7)
        self.G.add_edge(edge)

    def get_edges (self, node = None):
        if node:
            return list(self.G[node]).copy()
        else:
            return list(self.G.edges).copy() #  all edges
 
    def get_neighbours (self, node):
        return list(self.G.neighbors(node)).copy()

    
##################### Attributes ############################

    def is_node_attribute(self, name):
        attrs = nx.get_node_attributes(self.G, name)
        if attrs:
            return True
        return False

    def set_node_attribute(self, node = None, name = None, value = None, values_dict= None):
        if node and name and value is not None:
            if not self.is_node_attribute(name):
                self.set_all_attributes(name, None)
            self.G.nodes[node][name] = value
        elif values_dict:
            nx.set_node_attributes(self.G, values_dict)
        else:
            raise Exception ("you must enter: node, name, value OR values_dict")

    def set_all_attributes (self, name, value= None):
        nodes = self.G.nodes
        dic = {}
        for n in nodes:
            dic[n] = {name : value}
        self.set_node_attribute(values_dict=dic)
        
    def get_node_attribute(self, name, node = None ):
        if node:
            if name in self.G.nodes[node]:
                return copy.deepcopy(self.G.nodes[node][name])
        else:
            if self.is_node_attribute(name):
                return copy.deepcopy(nx.get_node_attributes(self.G, name))      
        return None
    
    def is_edge_attribute(self, name):
        attrs = nx.get_edge_attributes(self.G, name)
        if attrs:
            return True
        return False

    def get_edge_attribute(self, name, edge = None):
        if edge:
            dic = self.G.get_edge_data(*edge)
            if name in dic:
                return dic[name]
        else :
            return nx.get_edge_attributes(self.G, name)
        
    def set_edge_attribute(self, edge = None, name = None, value = None, values_dict = None):
        if edge and name and value is not None:
            if not self.is_edge_attribute(name):
                self.set_all_edge_attributes(name, None)
            u, v = edge
            self.G[u][v][name] = value
        elif values_dict:
            nx.set_edge_attributes(self.G, values_dict)
        else:
            raise Exception ("you must enter: edge, name, value OR values_dict")
    
    def set_all_edge_attributes(self, name, value = None):
        edges = self.get_edges()
        dic = {}
        for e in edges:
            dic[e] = {name : value}
        self.set_edge_attribute(values_dict=dic)
    
##################### Edges weights ############################

    def set_edge_weight (self, edge = None, weight = None, dict_values = None ):
        if edge and weight is not None:
            u, v = edge
            self.G[u][v]['weight'] = weight
        elif dict_values:
            #dict_values: {(u, v) : {'weight' : value}}
            self.set_edge_attribute(values_dict=dict_values)
        else:
            raise Exception("you must enter edge and weight or dict_values")

    def set_random_edges_weights(self, start, end):
        edges = self.get_edges()
        weights = {}
        for n in edges:
            weights[n] = {'weight' : random.randint(start, end)}

        self.set_edge_weight (dict_values=weights)

    def get_edge_weight (self, edge):
        weight = self.get_edge_attribute(edge=edge, name='weight')
        if weight is not None:
            return weight
        else:
            return 0
        

######################## Color #############################

    def __set_node_color_map_by_attributes (self):
        self.node_color_map.clear()
        for node in self.G:
            c =  self.get_node_attribute(node= node,name='color')
            if c:
                self.node_color_map.append(c)
            else:
                self.set_node_attribute(node, 'color', NODE_COLOR)
                self.node_color_map.append(NODE_COLOR)

    def set_all_nodes_color(self, color=NODE_COLOR):
        self.set_all_attributes('color', color)
        self.__set_node_color_map_by_attributes()

    def set_node_color (self, node = None, color = None, color_dic = None, node_list = None ):
        #color_dic = {node : 'color'}
        if node_list:
           color_dic = self.__list_to_color_dict(node_list, color)
        if node and color:
            self.set_node_attribute(node, 'color', color)
            self.__set_node_color_map_by_attributes()
        elif color_dic:
            attr_dict = {}
            for n in color_dic:
                attr_dict[n] = {'color' : color_dic[n]}
            self.set_node_attribute(values_dict=attr_dict)
            self.__set_node_color_map_by_attributes()
        elif color:
            self.set_all_nodes_color(color)
        else:
            raise Exception ("you must enter color OR color_dic / color_list")

    def __set_edge_color_map_by_attributes(self):
        self.edge_color_map.clear()
        for edge in self.get_edges():
            c =  self.get_edge_attribute(edge=edge, name= 'color')
            if c:
                self.edge_color_map.append(c)
            else:
                self.set_edge_attribute(edge, 'color', EDGE_COLOR)
                self.edge_color_map.append(EDGE_COLOR)

    def set_all_edges_color (self, color=EDGE_COLOR):
        self.set_all_edge_attributes('color', color)
        self.__set_edge_color_map_by_attributes()
    
    def set_edge_color (self, edge = None, color = None, color_dic = None):
        # color_dic = {(u, v): 'color'}
        if edge and color:
            self.set_edge_attribute(edge, 'color', color)
            self.__set_edge_color_map_by_attributes()
        elif color_dic:
            attr_dict = {}
            for n in color_dic:
                attr_dict[n] = {'color' : color_dic[n]}
            self.set_nodes_attributes(attr_dict)
            self.__set_node_color_map_by_attributes()
        elif color:
            self.set_all_edges_color(color)
        else:
            raise Exception ("you must enter edge, color OR color_dic")

    def __list_to_color_dict(self, node_list, color):
        color_dict = {}
        for node in node_list:
            color_dict[node] = color
        return color_dict

    def get_color_map_of_nodeList (self, nodeList = []):
        color_map = []
        for node in nodeList:
            color_map.append(self.get_node_attribute('color', node))
        return color_map

######################## Miscellaneous ####################

    def clear_path(self):
        self.path.clear()
    
    def is_tree(self):
        return nx.is_tree(self.G)

    def get_pos(self, node, layout='dot', root=None):
        pos = graphviz_layout(self.G, prog=layout, root=root)
        pos = pos[node]
        return pos

    def air_distance(self, start_node, end_node, layout='neato', root=None):
        pos = graphviz_layout(self.G, prog=layout, root=root)
        start_pos = pos[start_node]
        end_pos = pos[end_node]
        distance = ((start_pos[0]-end_pos[0])**2 + (start_pos[1]-end_pos[1])**2)**0.5
        # print (start_pos, end_pos)
        return distance

####################### Search functions ##################################

    def DFS_recursive (self, node):
        # tree only
        raise NotImplementedError
        
    def DFS_recursice_visited_check (self, node):
        raise NotImplementedError

    def DFS_stack (self, node):
        raise NotImplementedError
    
    def BFS (self, node):
        raise NotImplementedError

    def find_min_node(self, attribute = 'Q'):
        # use DFS with recurtion
        raise NotImplementedError

    def find_max_node(self, attribute = 'Q'):
        # use DFS with stack
        raise NotImplementedError

    def find_min_leaf(self, start):
        # use DFS with recurtion
        raise NotImplementedError

    def find_max_leaf(self, start):
        # use DFS with stack
        raise NotImplementedError

    def find_path_DFS (self, start, goal):
        raise NotImplementedError
    
    def find_path_BFS (self, start, goal):
        raise NotImplementedError

    def UCS (self, start, goal):
         #Dijkstra's
        raise NotImplementedError

    def Bellman_Ford (self, start, goal):
        raise NotImplementedError
    
    def aStar (self, start, goal, heuristic=None):
        raise NotImplementedError

################### minMax ##########################################

    def add_depth(self, root='1'):
        depth = 0
        visited = []
        frontier = [root]
        self.set_node_attribute(root, 'depth', depth)
        depth += 1
        while frontier:
            node = frontier.pop(0)
            visited.append(node)
            neighbors = self.get_neighbours(node)
            for n in neighbors:
                if n not in visited and n not in frontier:
                    frontier.append(n)
                    father_depth = self.get_node_attribute('depth', node)
                    self.set_node_attribute(n, 'depth', father_depth+1)

    def set_minmax_shape (self, start='max'):
        if start == 'max':
            bias = 0
        else:
            bias = 1
        self.add_depth()
        nodes = self.get_node_attribute(name='depth')
        for n in nodes:
            if (nodes[n]+bias) % 2 == 0:
                self.set_node_attribute(n, 'node_shape', '^')
            else:
                self.set_node_attribute(n, 'node_shape', 'v')

    def minMax (self, start, maxDepth = None):
        pass

    def minMax_alpha_beta(self, start, maxDepth = None):
        pass
