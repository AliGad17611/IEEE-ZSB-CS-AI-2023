lst = input().split()
list1=[]
list2=[]
for i in range(len(lst)):
    mid = len(lst[i])//2
    if len(lst[i])%2 != 0 :
        list1.append(lst[i][0:(mid+1)])
        list2.append(lst[i][(mid+1):])
    else:
        list1.append(lst[i][0:mid])
        list2.append(lst[i][mid:])
print(list1)
print(list2)