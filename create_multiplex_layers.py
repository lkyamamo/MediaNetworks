import csv
import os
import data_graphs.create_graph as cg
import networkx as nx
import matplotlib.pyplot as plt
import sys
#sys.path.append("Multiplex_optimal_percolation\Targeted_methods_python")
#import launch_targeted 

name = "integer_test_layer1"
directory_path = os.path.dirname(__file__)
file_path = "data/" + name + ".adjlist"
path = os.path.join(directory_path, file_path)


with open("multiplex_layers",'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name])
    writer.writerow([path])