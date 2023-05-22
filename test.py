import csv
import os
import data_graphs.create_graph as cg
import networkx as nx
import matplotlib.pyplot as plt
import sys
import data_graphs.create_graph as cg

#This file will take the data that is in the raw_data folder and create the respective networks of the data
dir_path = os.getcwd() + "/raw_data"

graphs = []

for file in os.scandir(dir_path):
    if(file.name[-2:] != "md"):

        graphs.append(cg.CreateGraph(file))

node_list1 = list(graphs[0].graph.nodes)
node_list2 = list(graphs[1].graph.nodes)
for i in range(len(node_list1)):
    if node_list1[i] != node_list2[i]:
        print("{0} and {1} ".format(node_list1[i], node_list2[i]))