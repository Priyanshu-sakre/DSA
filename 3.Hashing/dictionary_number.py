l1 = [1, 1, 2, 3, 4, 4, 5, 6, 7, 3, 4, 6, 2, 5, 7, 8]
dict_hash = {}
for i in l1:
    dict_hash[i] = l1.count(i)
print(dict_hash)
