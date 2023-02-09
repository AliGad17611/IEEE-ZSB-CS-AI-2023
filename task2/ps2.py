lst = list(map(int,input().split()))
list1 = []
even = list(filter(lambda x: x % 2 == 0 , lst))
print(len(even))