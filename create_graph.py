import os
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
import utility as util

#getting file path
directory_path = os.path.dirname(__file__)
original_comm_file = "data/network_original_comm.adjlist"
original_comm_path = os.path.join(directory_path, original_comm_file)

#creating unsorted graph
original_comm_graph = nx.read_weighted_edgelist(original_comm_path)

#creating bipartite arrangement with communities on the left and platforms on the right
communities = []
platforms = []

#seperating floating point (communities) nodes from non floating point nodes (platforms)
for node in original_comm_graph.nodes:
    test = node
    try:
        float(test)
        communities.append(node) 
    except:
        platforms.append(node)
    
ranking = []

for node in platforms:
    total = 0.0
    for edge in original_comm_graph.edges(node):
        total = total + float(edge[1])
    temp = (node, total)
    util.ranking(ranking, temp)

print(ranking)

#draw graph
pos = nx.bipartite_layout(original_comm_graph,communities)
nx.draw(original_comm_graph, pos, with_labels=True, font_weight='bold')
plt.show()