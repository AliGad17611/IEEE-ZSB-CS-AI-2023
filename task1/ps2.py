list1=[1,2,3,5,3,2,1]
list2=[1,2,3,4,5,3,2,1]
list3=[1,2,3,4,4,3,2,1]
def is_symmetric(lst):
    lst1 =len(lst)//2
    count = 0
    for i in range(0,lst1+1):
        if lst[i]!=lst[len(lst)-i-1]:
            count += 1
            break
    if count > 0:
        print("NOT SYMMETRIC")
    else:
        print("SYMMETRIC")
is_symmetric(list2)
is_symmetric(list1)
is_symmetric(list3)