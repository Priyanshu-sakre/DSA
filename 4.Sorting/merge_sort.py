def merge(arr, low, mid, high):
    temp = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    del temp  # to reduce the taken space


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)
    return arr


arr = [64, 25, 12, 22, 11]
n = len(arr)
print(merge_sort(arr, 0, n - 1))

"""
TC=O(NLOGN)
SC=O(N)
"""
