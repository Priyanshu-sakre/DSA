# floor-> largest element<=target
# ceil->smallest element>=target or lowerbound
def floor_ceil(arr, x):
    floor = ceil = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return x, x
        elif arr[mid] < x:
            floor = mid
            low = mid + 1
        else:
            ceil = mid
            high = mid - 1
    if floor != -1 and ceil != -1:
        return arr[floor], arr[ceil]
    elif floor == -1 and ceil != -1:
        return floor, arr[ceil]
    else:
        return arr[floor], ceil


arr = [3, 4, 7, 8, 8, 10]
print(floor_ceil(arr, 5))
