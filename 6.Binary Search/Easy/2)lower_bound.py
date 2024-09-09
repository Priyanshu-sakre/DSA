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


arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
print(lower_bound(arr, 11))
