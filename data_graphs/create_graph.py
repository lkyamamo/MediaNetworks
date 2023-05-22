import os
import networkx as nx
import matplotlib.pyplot as plt

class CreateGraph:

    #input: file of data to be parsed
    #has memeber variables: graph, communities, platforms
    def __init__(self, file_path):

        #creating unsorted graph
        self.graph = nx.read_weighted_edgelist(file_path)

        #creating bipartite arrangement with communities on the left and platforms on the right
        self.communities = []
        self.platforms = []

        #seperating floating point (communities) nodes from non floating point nodes (platforms)
        for node in self.graph.nodes:
            test = node
            try:
                float(test)
                self.communities.append(node) 
            except:
                self.platforms.append(node)

        
