arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
n = len(arr)
k = 3


# brute
def longest_subarray(arr, n, k):
    l1 = 0
    for i in range(n):
        sum1 = 0
        for j in range(i, n):
            sum1 += arr[j]
            if sum1 == k:
                l1 = max(l1, j - i + 1)
    return l1


"""
TC->O(N^2)
SC->O(1)
"""


print(longest_subarray(arr, n, k))


# better
def longest_subarray2(arr, n, k):
    hash_map = {}
    sum1 = 0
    maxx = 0
    for i in range(n):
        sum1 += arr[i]
        if sum1 == k:
            maxx = i + 1

        rem = sum1 - k
        if rem in hash_map:
            l = i - hash_map[rem]
            maxx = max(l, maxx)
        if sum1 not in hash_map:
            hash_map[sum1] = i
    return maxx


print(longest_subarray2(arr, n, k))

"""
TC->O(N)
SC->O(N)
"""


# optimal
def longest_subarray3(arr, n, k):
    sum1 = arr[0]
    i = j = 0
    maxL = 0
    while j < n:
        while i<=j and sum1 > k:
            sum1 -= arr[i]
            i += 1
        if sum1 == k:
            maxL = max(maxL, j - i + 1)
        j += 1
        if j < n:
            sum1 += arr[j]
    return maxL


print(longest_subarray3(arr, n, k))
