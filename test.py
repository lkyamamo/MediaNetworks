import csv
import os
import data_graphs.create_graph as cg
import networkx as nx
import matplotlib.pyplot as plt
import sys
import data_graphs.create_graph as cg

#This file will take the data that is in the raw_data folder and create the respective networks of the data
dir_path = os.getcwd() + "\raw_data"

graphs = []

for file in os.scandir(dir_path):
    graphs.append(cg.CreateGraph(file.path))