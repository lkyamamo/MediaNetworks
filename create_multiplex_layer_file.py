import csv
import os
import data_graphs.create_graph as cg
import networkx as nx
import matplotlib.pyplot as plt
import sys
import data_graphs.create_graph as cg


#This file will take the integer converted data and create the respective layers
dir_path = os.getcwd() + "/data"

graphs = []

for file in os.scandir(dir_path):
    if(file.name != "mapping.txt"):
        graphs.append(cg.CreateGraph(file))


#it will print the number of total nodes (each layer should have the same number of nodes)
print(len(graphs[0].nodes))

#it will output files that will be an unweighted edge list into the "data" directory


#a mapping will be created from the integer layer number to the initial raw data file


#it will write a file that will be in the format of the wanted "multiplex_layer" file format to be used in the launch_targeted

name = "integer_test_layer1"
directory_path = os.path.dirname(__file__)
file_path = "data/" + name + ".adjlist"
path = os.path.join(directory_path, file_path)


with open("multiplex_layers",'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name])
    writer.writerow([path])