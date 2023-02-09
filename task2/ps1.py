def sort(lst):
    lst1 = list(map(int,lst))
    list1 = []
    while len(lst1)>0:
        list1.append(min(lst1))
        lst1.remove(min(lst1))
    print(list1)
sort(input().split())