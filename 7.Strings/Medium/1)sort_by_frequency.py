def sort_frequency(a):
    s = ""
    hash_map = {}
    for i in a:
        hash_map[i] = hash_map.get(i, 0) + 1
    print(hash_map)
    hash_map1 = dict(sorted(hash_map.items(), key=lambda i: i[1], reverse=True))
    print(hash_map1)
    for i in hash_map1:
        s += i * hash_map1[i]
    return s


a = "Aabb"
print(sort_frequency(a))
