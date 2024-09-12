# brute
def peak(arr):
    for i in range(len(arr)):
        if (i == 0 or arr[i - 1] < arr[i]) and (
            i == len(arr) - 1 or arr[i] > arr[i + 1]
        ):
            return i


arr = [1, 8, 1, 5, 3]
print(peak(arr))


# optimal
def peak2(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] > arr[mid - 1]:
            low = mid + 1
        elif arr[mid] > arr[mid + 1]:
            high = mid - 1
        ##only when peak element>1##
        else:
            low = mid + 1
        ############################
    return -1


arr = [1, 8, 1, 5, 3]
print(peak2(arr))
