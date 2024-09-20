def remove_parenthesis(s):
    str1 = ""
    count = 1
    i = 0
    for j in range(1, len(s)):
        if s[j] == "(":
            count += 1
        else:
            count -= 1
            if count == 0:
                str1 += s[i + 1 : j]
                i = j + 1
    return str1


s = "(()())(())(()(()))"
print(remove_parenthesis(s))
