import os
import networkx as nx
import matplotlib.pyplot as plt
import utility as util

file_name = "network_original_comm"

#getting file path
directory_path = os.path.dirname(__file__)
file = "data/network_original_comm.adjlist"
path = os.path.join(directory_path, file)

#creating unsorted graph
graph = nx.read_weighted_edgelist(path)

#creating bipartite arrangement with communities on the left and platforms on the right
communities = []
platforms = []

#seperating floating point (communities) nodes from non floating point nodes (platforms)
util.seperate(communities, platforms, graph)

print(graph.edges(platforms[0]))

#ranking the amount of total retweets for each platform in original_comm dataset and outputing to text file 
util.rank_total_weight(file_name + "_retweet_ranking", graph, platforms)

#ranking amount of total communities that retweeted the platform's original post
util.rank_total_spread(file_name + "_total_communities_ranking", graph, platforms)

#draw graph
pos = nx.bipartite_layout(graph, communities)
nx.draw(graph, pos, with_labels=True, font_weight='bold')
