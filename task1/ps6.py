n = input().split(",")
girls = input().split(",")
for i in range(len(girls)):
    n.append(girls[i])
dict1 = {}
for i in range(len(n)):
    s = n[i].split(":")
    dict1[s[0]] = int(s[1])
print(dict1)
