def zeros3(arr, n):
    temp = []
    for i in arr:
        if i != 0:
            temp.append(i)
    for i in range(n - len(temp), n):
        arr[i] = temp[i - (n - len(temp))]
    for i in range(n - len(temp)):
        arr[i] = 0
    del temp
    return arr


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = len(arr)
print(zeros3(arr, n))
