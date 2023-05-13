#ranking will be a top n weights
#will be a list of tuples (node, total weight)
length = 10
def ranking(ranking, current):

    #over all tuples things in the ranking
    for i in range(len(ranking)):
        #if has a greater out weight then swap with it
        if current[1] > ranking[i][1]:
            temp = ranking[i]
            ranking[i] = current
            current = temp
    
    if len(ranking) < length:
        ranking.append(current)

