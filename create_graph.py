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
util.seperate(communities, platforms, original_comm_graph)

#ranking the amount of total retweets for each platform in original_comm dataset and outputing to text file 
util.rank_total_weight("original_comm_retweet_ranking", original_comm_graph, platforms)

#ranking amount of total communities that retweeted the platform's original post
util.rank_total_spread("original_comm_total_communities_ranking", original_comm_graph, platforms)

#draw graph
pos = nx.bipartite_layout(original_comm_graph,communities)
nx.draw(original_comm_graph, pos, with_labels=True, font_weight='bold')
plt.show()