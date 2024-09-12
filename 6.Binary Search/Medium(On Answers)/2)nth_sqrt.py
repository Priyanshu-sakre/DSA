# brute
def sqrt1(n, m):
    ans = -1
    for i in range(1, m + 1):
        if i * i == m:
            return i
    return -1


print(sqrt1(2, 9))


# optimal
def sqrt2(n, m):
    low = 1
    high = m
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if mid**n == m:
            return mid
        elif mid**n < m:
            low = mid + 1
        else:
            high = mid - 1
    return ans


print(sqrt2(2, 9))
