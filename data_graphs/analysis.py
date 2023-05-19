import data_graphs.create_graph as cg
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append("Multiplex_optimal_percolation\Targeted_methods_python")
import launch_targeted 

original = cg.CreateGraph("network_original_comm")
quoted_tweet = cg.CreateGraph("network_quoted_tweet_comm")
reply = cg.CreateGraph("network_reply_comm")
retweeted_wo_comment = cg.CreateGraph("network_retweeted_tweet_without_comment_comm")

plt.show()

