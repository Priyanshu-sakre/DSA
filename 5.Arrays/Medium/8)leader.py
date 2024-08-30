# brute 1 & 2
def leaders(n, arr):
    leader = []
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[i] >= arr[j]:
                count += 1
            else:
                break
        if count == n - i - 1:
            if arr[i] not in leader:  # only if we need unique
                leader.append(arr[i])
    return leader
    # return sorted(leader)  if need sorted list


arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
print(leaders(n, arr))


# optimal
def leaders2(n, arr):
    leader = []
    maxi = 0
    for i in range(n - 1, -1, -1):
        if arr[i] >= maxi:
            leader.append(arr[i])
            maxi = arr[i]
    return list(reversed(leader))


print(leaders2(n, arr))
