def longest_common_prefix(strs):
    str1 = ""
    strs.sort()
    a = strs[0]
    b = strs[-1]
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            str1 += a[i]
        else:
            break
    return str1


strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))
