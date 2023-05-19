import os
import networkx as nx
import matplotlib.pyplot as plt
import utility as util
import heaps

#, ('four', 4), ('five', 5), ('six', 6)
mylist = [('one', 1), ('two', 2), ('three', 3)]

myHeap = heaps.Heap(mylist)

print(myHeap.heap)