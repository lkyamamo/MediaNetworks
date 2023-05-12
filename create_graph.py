import os
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

#getting file path
absolute_path = os.path.dirname(__file__)
relative_path = "data/network_original_comm.adjlist"
full_path = os.path.join(absolute_path, relative_path)

#creating unsorted graph
G = nx.read_weighted_edgelist(full_path)

#creating bipartite arrangement with communities on the left and platforms on the right
communities = []
platforms = []

#seperating floating point (communities) nodes from non floating point nodes (platforms)
for node in G.nodes:
    test = node
    try:
        float(test)
        communities.append(node) 
    except:
        platforms.append(node)
    

#draw graph
pos = nx.bipartite_layout(G,communities)
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.show()