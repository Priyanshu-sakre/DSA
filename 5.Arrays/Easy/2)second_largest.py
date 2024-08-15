arr = [12, 35, 1, 10, 34, 1]
largest = arr[0]
sec_largest = 0
for i in arr:
    if i > largest and i > sec_largest:
        sec_largest = largest
        largest = i
    elif i < largest and i > sec_largest:
        sec_largest = i
print(sec_largest)
