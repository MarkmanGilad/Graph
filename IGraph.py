# need to install graphviz and c++
# https://pygraphviz.github.io/
# https://pygraphviz.github.io/documentation/stable/install.html
# pip install --global-option=build_ext --global-option="-IC:\Program Files\Graphviz\include" --global-option="-LC:\Program Files\Graphviz\lib" pygraphviz
# pip install typing-extensions - not sure

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import os
import copy


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
        self.set_empty_attributes('path')
        self.set_empty_attributes('weight')
        self.set_all_nodes_color(NODE_COLOR)
        self.set_edges_color([],'')
    
    def save_to_dotFile (self, path):
        dir = os.path.dirname(__file__)
        full_path = os.path.join(dir, path)
        nx.nx_agraph.write_dot(self.G, full_path)

    def draw (self, layout='dot'):
        # plt.show() in main
        # version but may include: ‘dot’, ‘twopi’, ‘fdp’, ‘sfdp’, ‘circo’, 'neato'
        self.pos = graphviz_layout(self.G, prog=layout)
        nx.draw(self.G, self.pos, **self.options)
        labels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx_edge_labels(self.G,self.pos,edge_labels=labels)

    def get_nodes (self):
        return list(self.G.nodes)

    def add_node (self, node):
        self.G.add_node(node)

    def get_edges (self, node):
        return list(self.G[node])

    def get_all_edges (self):
        return list(self.G.edges).copy()

    def add_edge (self, edge):  # edge = (5, 7)
        self.G.add_edge(edge)
    
    def get_neighbours (self, node):
        return list(self.G.neighbors(node)).copy()
    
    def set_edge_weight (self, edge, weight):
        u, v = edge
        self.G[u][v]['weight'] = weight
        
    def get_edge_weight (self, edge):
        u, v = edge
        return self.G[u][v]['weight']

    def set_edges_weights (self, dict_values):
        #dict_values: {(u, v) : {weight : value}}
        nx.set_edge_attributes(self.G, dict_values)

    def set_all_nodes_color(self, color=NODE_COLOR):
        self.node_color_map.clear()
        for n in self.G:
            self.node_color_map.append(color)

    def set_nodes_color (self, nodes, color):
        if not self.node_color_map:
            self.set_all_nodes_color()
        new_color_map = []
        i = 0
        for n in self.G:
            if n in nodes:
                new_color_map.append(color)
            else:
                new_color_map.append(self.node_color_map[i])
            i+=1
        self.node_color_map.clear()
        self.node_color_map += new_color_map

    def set_node_color (self, node, color):
        if len(self.node_color_map) == 0:
            self.set_all_nodes_color()
        index = list(self.G).index(node)
        self.node_color_map[index] = color

    def set_all_edges_color (self, color=EDGE_COLOR):
        self.edge_color_map.clear()
        for n in self.G.edges(data=False):
            self.edge_color_map.append(color)

    def set_edges_color (self, edges, color):
        # self.edge_color_map.clear()
        # for n in self.G.edges(data=False):
        #     if n in edges:
        #         self.edge_color_map.append(color)
        #     else:
        #         self.edge_color_map.append(EDGE_COLOR)
        if not self.edge_color_map:
            self.set_all_edges_color(EDGE_COLOR)
        new_edge_color_map = []
        i = 0
        for n in self.G.edges(data=False):
            if n in edges:
                self.edge_color_map.append(color)
            else:
                self.edge_color_map.append(self.edge_color_map[i])
            i+=1

        self.edge_color_map.clear()
        self.edge_color_map += new_edge_color_map

    def set_edge_color (self, edge, color):
        if len(self.edge_color_map) == 0:
            self.set_all_edges_color()
        index = list(self.G.edges(data=False)).index(edge)
        self.edge_color_map[index] = color

    def is_node_attribute(self, name):
        attrs = nx.get_node_attributes(self.G, name)
        if attrs:
            return True
        return False

    def set_empty_attributes (self, name):
        nodes = self.G.nodes
        dic = {}
        for n in nodes:
            dic[n] = {name:[]}
        nx.set_node_attributes(self.G, dic)

    def set_nodes_attribure(self, nodes, name, values):
        # name = attr name string; nodes = list of nodes; values = list of attr values
        
        if not self.is_node_attribute(name):
            self.set_empty_attributes(name)
        for n in range(len(nodes)):
            self.G[nodes[n]][name] = values[n]

    def set_node_attribute(self, node, name, value):
        if not self.is_node_attribute(name):
            self.set_empty_attributes(name)
        self.G.nodes[node][name] = value
        
    def get_node_attribute(self, node, name):
        return copy.deepcopy(self.G.nodes[node][name])

    def clear_path(self):
        self.path.clear()
    
    #########################################################

    def DFS_recursive (self, node):
        # tree only
        raise NotImplementedError
        
    def DFS_recursice_visited_check (self, node):
        raise NotImplementedError

    def DFS_stack (self, node):
        raise NotImplementedError
    
    def BFS (self, node):
        raise NotImplementedError

    def find_path_DFS (self, start, goal):
        raise NotImplementedError
    
    def find_path_BFS (self, start, goal):
        raise NotImplementedError

    def UCS (self, start, goal):
         #Dijkstra's
        raise NotImplementedError

    def Bellman_ford (self, start, goal):
        raise NotImplementedError
    