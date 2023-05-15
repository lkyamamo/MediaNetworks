

#ranking will be a top n weights
#will be a list of tuples (node, total weight)
length = 100000

def ranking(rank, current):

    #over all tuples things in the ranking
    for i in range(len(rank)):
        #if has a greater out weight then swap with it
        if current[1] > rank[i][1]:
            temp = rank[i]
            rank[i] = current
            current = temp
    
    if len(rank) < length:
        rank.append(current)
    

#will take a list as an input and save the list as a ranking in a text file in text_files folder
def save_list(rank, name, labels):
    f = open("text_files/" + name + ".txt", "w", encoding="utf-8")
    f.write(labels)
    for i in range(len(rank)):
        f.write(str(i + 1) + "\t" + rank[i][0] + "\t" + str(rank[i][1]))
        #f.write("{}".format(i))
        f.write("\n")

#inputs: name of the output file, graph that was created from the dataset, platforms from the input dataset
#output: a text file that ranks the total outgoing weights for all the platforms in the given graph
def rank_total_weight(name, G, platforms):
    rank = []
    for node in platforms:
        total = 0.0
        for edge in G.edges(node):
            total = total + float(edge[1])
        temp = (node, total)
        ranking(rank, temp)

    save_list(rank, name, "Rank \t Platform \t Retweets \n \n")

#inputs: name of the output file, graph that was created from the dataset, platforms from the input dataset
#output: text file that ranks the platforms by total amount of edges going out of it
def rank_total_spread(name, G, platforms):
    rank = []
    for node in platforms:
        total = 0
        for edge in G.edges(node):
            total += 1
        temp = (node, total)
        ranking(rank, temp)

    save_list(rank, name, "Rank \t Platform \t Total Communities \n \n")


