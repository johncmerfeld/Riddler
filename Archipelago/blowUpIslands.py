import networkx as nx
import random as rand
import numpy as np
import pandas as pd

def blowUpIslands(n, p):
   
    G = nx.random_tree(n)
    for i in range(0, n):
        if rand.random() < p:
            G.remove_node(i)
    
    return nx.number_connected_components(G)

# run a bunch of trials to get an average
def testOutcomes(n, p, Ntrials):
    
    results = []
    for i in range(0, Ntrials):
        results.append(blowUpIslands(n, p))
    
    return np.mean(results)

output = []

for n in range(5, 100):
    for j in range(1, 100):
        p = j / 100
        d = {
            'n' : n,
            'p' : p,
            'communities' : testOutcomes(n, p, 20) 
        }
        output.append(d)
        
output = pd.DataFrame(output)
        
output.to_csv('CommunitiesLeft.csv')

