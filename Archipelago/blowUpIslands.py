import networkx as nx
import matplotlib.pyplot as plt
import random as rand

n = 20
p = 0.1

G = nx.random_tree(n)
for i in range(0, n):
    if rand.random() < p:
        G.remove_node(i)
        
nx.draw(G, nodecolor='g', edge_color='b')