dict1 = {
    "A": [20, 30, 100, 49],
    "B": [00, 199, 201, 29],
    "C": [40, 90, 69, 18]
}
largest_range_key = "A"
largest_range = current_range = 0
for key , value in dict1.items():
    current_range = max(value)-min(value)
    if largest_range <=current_range:
        largest_range=current_range
        largest_range_key =key
print(largest_range_key,largest_range)