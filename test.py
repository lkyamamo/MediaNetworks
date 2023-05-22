import csv
import os
import data_graphs.create_graph as cg
import networkx as nx
import matplotlib.pyplot as plt
import sys
import data_graphs.create_graph as cg
import numpy as np

results_dict = {'a': [1,2,3],
                'b': [2,3,4],
                'c': [3,4,5],
                'd': [4,5,6]}

with open("output.txt","w") as f:
    for key,value in results_dict.items():
        f.write("{0} {1}".format(key, value))
        f.write("\n")