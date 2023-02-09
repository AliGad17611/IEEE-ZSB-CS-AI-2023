file = open("grades.txt","r")
lst = file.readlines()
list1 = []
dict1 = {}
id = sum1 = highest_score = 0
oldest = 2100
for i in range(1,len(lst)):
    list1.append(lst[i].split())
    list1[i-1].remove("-")
    list1[i - 1].remove(":")
for i in range(len(list1)):
    if list1[i][2] == 'N/A':
        continue
    dict1[int(list1[i][0])] = {'name': list1[i][1], 'score': int(list1[i][2]), 'birthyear': int(list1[i][3]), 'gender': list1[i][4]}
    if oldest>int(list1[i][3]):
        oldest = int(list1[i][3])
        id = int(list1[i][0])
    sum1 += int(list1[i][2])
    if highest_score < int(list1[i][2]):
        highest_score = int(list1[i][2])
        gender1 = list1[i][4]
print("A)",dict1)
print("B)",id)
print("C)",sum1/len(dict1))
print("D)",gender1)
file.close()