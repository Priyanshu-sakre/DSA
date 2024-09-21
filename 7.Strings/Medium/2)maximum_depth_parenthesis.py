def maximum_depth(s):
    count = 0
    max_count = 0
    for i in s:
        if i == "(":
            count += 1
            max_count = max(count, max_count)
        elif i == ")":
            count -= 1
    return max_count


s = "(1+(2*3)+((8)/4))+1"
print(maximum_depth(s))
