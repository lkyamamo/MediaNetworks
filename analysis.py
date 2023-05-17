import create_graph as cg
import networkx as nx
import matplotlib.pyplot as plt

original = cg.CreateGraph("network_original_comm")
quoted_tweet = cg.CreateGraph("network_quoted_tweet_comm")
reply = cg.CreateGraph("network_reply_comm")
retweeted_wo_comment = cg.CreateGraph("network_retweeted_tweet_without_comment_comm")

plt.show()

