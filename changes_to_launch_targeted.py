###### Results
results_dict={
"HDA":(HDA_size_nodes, HDA_total_target_nodes),
"EMD1step":(EMD1step_size_nodes, EMD1step_total_target_nodes),
"EMD":(EMD_size_nodes,EMD_total_target_nodes),
"DCI":(DCI_size_nodes,DCI_total_target_nodes),
"DCIz":(DCIz_size_nodes,DCIz_total_target_nodes),
"kcore-EMD1step":(kcore_EMD1step_ideal_size_nodes,kcore_EMD1step_ideal_total_target_nodes),
"kcore-EMD":(kcore_EMD_ideal_size_nodes,kcore_EMD_ideal_total_target_nodes),
"kcore-DCI":(kcore_DCI_size_nodes,kcore_DCI_total_target_nodes),
"kcore-DCIz":(kcore_DCIz_size_nodes,kcore_DCIz_total_target_nodes),
"CoreHD-EMD1step":(CoreHD_EMD1step_size_nodes,CoreHD_EMD1step_total_target_nodes),
"CoreHD-EMD":(CoreHD_EMD_size_nodes,CoreHD_EMD_total_target_nodes),
"CoreHD-DCI":(CoreHD_DCI_size_nodes,CoreHD_DCI_total_target_nodes),
"CoreHD-DCIz":(CoreHD_DCIz_size_nodes,CoreHD_DCIz_total_target_nodes),
"CI2-EMD1step":(CI_2_EMD1step_size_nodes,CI_2_EMD1step_total_target_nodes),
"CI2-EMD":(CI_2_EMD_size_nodes,CI_2_EMD_total_target_nodes),
"CI2-DCI":(CI_2_DCI_size_nodes,CI_2_DCI_total_target_nodes),
"CI2-DCIz":(CI_2_DCIz_size_nodes,CI_2_DCIz_total_target_nodes),
"BPD-EMD1step":(BPD_EMD1step_size_nodes,BPD_EMD1step_total_target_nodes),
"BPD-EMD":(BPD_EMD_size_nodes,BPD_EMD_total_target_nodes),
"BPD-DCI":(BPD_DCI_size_nodes,BPD_DCI_total_target_nodes),
"BPD-DCIz":(BPD_DCIz_size_nodes,BPD_DCIz_total_target_nodes),
"CoreHD - CoreHD":(Pure_CoreHD_size_nodes,Pure_CoreHD_total_target_nodes),
"CI2 - CI2":(Pure_CI_2_size_nodes,Pure_CI_2_total_target_nodes),
"BPD - BPD":(PureBPD_size_nodes,PureBPD_total_target_nodes)}


#print(sorted(results_dict.items(),key= lambda x: x[1]))

with open("output.txt","w") as f:
    for key,value in results_dict.items():
        f.write("{0} {1}".format(key, value))
        f.write("\n")
    
