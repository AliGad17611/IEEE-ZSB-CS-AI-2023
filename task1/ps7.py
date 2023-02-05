lst = list(map(int,input().split()))
k = int(input())
list1 = []
for i in range(len(lst)-k,len(lst)):
    list1.append(lst[i])
for i in range(0,len(lst)-k):
    list1.append(lst[i])
print(list1)