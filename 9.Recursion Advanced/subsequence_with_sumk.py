arr = [1, 2, 3]
ans = []
a = []
i = 0
sum1 = 0
target = 5


def subset(arr, ans, a, i, sum1, target):
    if i == len(arr):
        if sum1 == target:
            ans.append(a.copy())
        return
    subset(arr, ans, a, i + 1, sum1, target)
    a.append(arr[i])
    subset(arr, ans, a, i + 1, sum1 + arr[i], target)
    a.pop()


subset(arr, ans, a, i, sum1, target)
print(ans)
