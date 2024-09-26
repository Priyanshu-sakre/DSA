l1 = [1, 2, 2, 3, 3, 4, 5, 6]
l2 = [2, 3, 3, 5, 6, 6, 7]
n = len(l1)
m = len(l2)


# brute
def intersection(l1, l2, n, m):
    visit = [0] * min(n,m)
    intersect = []
    for i in range(n):
        for j in range(m):
            if l1[i] == l2[j] and visit[j] == 0:
                intersect.append(l1[i])
                visit[j] = 1
                break
            if l2[j] > l1[i]:
                break
    return intersect


print(intersection(l1, l2, n, m))


# optimal
def intersection2(l1, l2, n, m):
    intersect2 = []
    i = j = 0
    while i < n and j < m:
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            intersect2.append(l1[i])
            i += 1
            j += 1
    return intersect2


print(intersection2(l1, l2, n, m))
