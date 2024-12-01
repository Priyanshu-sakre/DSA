s = "geeks for geeks"
pat = "geek"
index = s.find(pat)
while index >= 0:
    print(index, end=" ")
    index = s.find(pat, index + 1)
