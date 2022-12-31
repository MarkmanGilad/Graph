
from random import random
from iGraph import nxGraph
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

G = nxGraph()

#G.set_from_dotFile('GraphsFiles/test.dot')
G.set_from_dotFile('GraphsFiles/biGraph.dot')
G.set_nodes_color([], None)
G.set_edges_color([], None)

fig = plt.figure()
net = fig.add_subplot()
nodes = G.get_nodes()
i = 0
c = 'r'
def animate(frame):
    global i
    global c
    n = nodes[i]
    G.set_node_color(n, c)
    plt.clf()
    plt.cla()
    G.draw()
    if i == len(nodes)-1:
        i=0
        if c == 'r':
            c = 'b'
        else:
            c = 'r' 
    else:
        i+=1

ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()

