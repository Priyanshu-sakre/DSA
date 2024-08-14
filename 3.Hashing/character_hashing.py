str1 = "aaeerrooppllaannee"
l1 = [0] * 26
for i in str1:
    l1[ord(i) - 97] += 1
print(l1)
