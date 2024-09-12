# brute
import math

print(int(math.sqrt(28)))


# better
def sqrt1(n):
    ans = 1
    for i in range(1, n + 1):
        if i * i <= n:
            ans = i
        else:
            break
    return ans


print(sqrt1(28))


# optimal
def sqrt2(n):
    low = 1
    high = n
    ans = 1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


print(sqrt2(28))
