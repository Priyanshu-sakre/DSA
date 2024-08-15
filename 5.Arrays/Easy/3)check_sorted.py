# optimal


def issorted(n, arr):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print(issorted(n, arr))

# brute


def issorted2(n, arr):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False
    return True


print(issorted2(n, arr))
