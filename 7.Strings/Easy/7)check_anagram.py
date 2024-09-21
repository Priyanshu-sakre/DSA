def anagram(a, b):
    a1 = sorted(list(a))
    b1 = sorted(list(b))
    if len(a1) == len(b1) and a1 == b1:
        return True
    else:
        return False


a = "anagram"
b = "nagaram"
print(anagram(a, b))
