from ps4 import dict1
filter_file = open("filtered.txt","w")
filter_file.write("id name - birthyear")
for i in dict1:
    filter_file.write("\n{} {} - {}".format(i,dict1[i]["name"],dict1[i]["birthyear"]))
filter_file.close()