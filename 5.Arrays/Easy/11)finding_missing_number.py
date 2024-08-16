# brute
arr = [1, 2, 4, 5]
N = 5


def find(arr, N):
    for i in range(1, N + 1):
        if i not in arr:
            return i


print(find(arr, N))

# sum method
sum1 = (N * (N + 1)) // 2
sum2 = sum(arr)
print(sum1 - sum2)

# xor method
xor1 = 0
xor2 = 0
for i in range(1, len(arr)):
    xor1 = xor1 ^ arr[i]
    xor2 = xor2 ^ (i + 1)
xor2 = xor2 ^ N
print(xor1 ^ xor2)
