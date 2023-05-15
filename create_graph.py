import os
import networkx as nx
import matplotlib.pyplot as plt
import utility as util

class CreateGraph:

    #input: file name of data to be parsed
    #has memeber variables: graph, communities, platforms
    def __init__(self, file_name):

        #getting file path
        directory_path = os.path.dirname(__file__)
        file = "data/" + file_name + ".adjlist"
        path = os.path.join(directory_path, file)

        #creating unsorted graph
        self.graph = nx.read_weighted_edgelist(path)

        #creating bipartite arrangement with communities on the left and platforms on the right
        self.communities = []
        self.platforms = []

        #seperating floating point (communities) nodes from non floating point nodes (platforms)
        #seperating floating point (communities) nodes from non floating point nodes (platforms)
        for node in self.graph.nodes:
            test = node
            try:
                float(test)
                self.communities.append(node) 
            except:
                self.platforms.append(node)

        #ranking the amount of total retweets for each platform in original_comm dataset and outputing to text file 
        util.rank_total_weight(file_name + "_retweet_ranking", self.graph, self.platforms)

        #ranking amount of total communities that retweeted the platform's original post
        util.rank_total_spread(file_name + "_total_communities_ranking", self.graph, self.platforms)

        #draw graph
        pos = nx.bipartite_layout(self.graph, self.communities)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold')
