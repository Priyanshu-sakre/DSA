# without binary search
arr = [5, 7, 7, 8, 8, 10]
first = -1
last = -1
for i in range(len(arr)):
    if arr[i] == 6:
        if first == -1:
            first = i
            # last = i
        last = i
print([first, last])


# with upper bound and lower bound
def lower_bound(arr, target):
    ans = len(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def upper_bound(arr, target):
    ans = len(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def first_last(arr, target):
    l = lower_bound(arr, target)
    u = upper_bound(arr, target)
    if l == len(arr) or arr[l] != target:
        return [-1, -1]
    return [l, u - 1]


arr = [5, 7, 7, 8, 8, 10]
target = 6
print(first_last(arr, target))


# with binary search
def first_last(arr, target):
    first = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    last = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if first == -1:
        return [-1, -1]
    else:
        return [first, last]


arr = [5, 7, 7, 8, 8, 10]
print(first_last(arr, 6))
