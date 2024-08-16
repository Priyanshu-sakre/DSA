arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
n = len(arr)
k = 3


def longest_subarray(arr, n, k):
    l1 = 0
    for i in range(n):
        sum1 = 0
        for j in range(i, n):
            sum1 += arr[j]
            if sum1 == k:
                l1 = max(l1, j - i + 1)
    return l1


print(longest_subarray(arr, n, k))
