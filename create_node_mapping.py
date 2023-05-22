#takes in one of the layers and creates an integer node mapping and outputs it into a file in the following format
#   node_name   integer_value


import csv
import os
import data_graphs.create_graph as cg
import networkx as nx
import matplotlib.pyplot as plt
import sys
import data_graphs.create_graph as cg

#create graph of a node layer
G = cg.CreateGraph("/home/lkyamamoto/Research/MediaNetworks/raw_data/network_original_comm.adjlist")

#get node list
node_list = list(G.graph.nodes)

#write mapping 
with open("mapping.txt", 'w') as f:
    for i in range(len(node_list)):
        f.write("{0} {1}".format(node_list[i], i))
        f.write('\n')
