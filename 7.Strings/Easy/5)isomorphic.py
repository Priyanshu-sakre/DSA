def isomorphic(a, b):
    hash_map = {}
    for i in range(len(a)):
        if a[i] not in hash_map and b[i] in hash_map.values():
            return False
        hash_map[a[i]] = b[i]
    for i in range(len(a)):
        if hash_map[a[i]] != b[i]:
            return False
    return True


a = "paper"
b = "title"
print(isomorphic(a, b))
