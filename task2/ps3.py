lst = list(map(int,input().split()))
list1 = lst
largest_num = []
largest = small = 0
small_num =[]
for i in range(len(lst)):
    if lst[i]>0:
        largest += lst[i]
        largest_num.append(lst[i])
while len(small_num)<2:
    small += min(list1)
    small_num.append(min(list1))
    list1.remove(min(list1))
print("{} ({})".format(largest_num,largest))
print("{} ({})".format(small_num,small))