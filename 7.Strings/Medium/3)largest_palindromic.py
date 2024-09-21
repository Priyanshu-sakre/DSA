def largest(s):
    maxi = 0
    str1 = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            s1 = s[i : j + 1]
            if s1 == s1[::-1] and j - i + 1 > maxi:
                str1 = s1
                maxi = j - i + 1
    return str1


s = "babad"
print(largest(s))
