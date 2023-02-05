lst = list(map(int,input().split()))
target = int(input())
count = 0
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        temp = lst[i]+lst[j]
        if temp == target :
            if count >0:
                print(", ",end="")
            print(f"{i}, {j}",end="")
            count += 1
if count == 0:
    print("not founded")