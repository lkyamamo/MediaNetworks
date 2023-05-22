import re

#this will be a list of sets with the following definitions
#output_list[0]: union of union of all algorithms' target node sets for each duplex
#output_list[1]: union of intersections of all algorithms' target node sets for each duplex
#output_list[2]: intersection of unions of all algorithms' target node sets for each duplex
#output_list[3]: intersection of intersections of all algorithms' target node sets for each duplex
output_list = [set(),set(),set(),set()]

#create total set of all nodes
N = 278
total_set = set()
for i in range(N):
    total_set.add(i)

for i in range(3):
    for j in range(i+1):
        #get the union set and intersecting set of each algorithm target node set
        union_set = set()
        intersecting_set = total_set

        with open("results/{0}_{1}_results.txt".format(2-i,3-j), "r") as f:
            for line in f:
                # create node list from input
                node_list = re.findall(r'\[(.*?)\]', line)
                node_list[0] = node_list[0][1:]
                node_list = [int(float(number)) for number in node_list]
                
                #turn list into a set
                node_set = set(node_list)

                #union set and subtract from total possible set
                union_set = set.union(node_set,union_set)
                intersecting_set = set.intersection(intersecting_set, node_set)
        
        #at this point have the intersection and union of all node sets from algorithms
        #adding to output list of sets
        output_list[0] = set.union(output_list[0], union_set)
        output_list[1] = set.union(output_list[1], intersecting_set)
        
        if i == 0 & j == 0:
            output_list[2] = union_set
            output_list[3] = intersecting_set
        else:
            output_list[2] = set.intersection(output_list[2], union_set)
            output_list[3] = set.intersection(output_list[3], intersecting_set)

#convert integer nodes back to string labels
#create dictionary from mapping file
mapping = {}
with open("data/mapping.txt", "r") as f:
    for line in f:
        split_line = line.split(' ')
        mapping[int(split_line[1])] = split_line[0]
        


#write onto an output file
with open("duplex_results.txt", "w") as f:
    for set in output_list:
        for element in set:
            f.write(str(mapping[element]))
            f.write(" ")
        f.write("\n")