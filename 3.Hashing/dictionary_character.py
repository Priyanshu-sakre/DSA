str1 = "aaeerrooppllaannee"
dict_hash = {}
for i in str1:
    dict_hash[i] = dict_hash.get(i, 0) + 1
print(dict_hash)
