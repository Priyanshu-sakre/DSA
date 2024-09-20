def reverse_word(s):
    ls = s.split()
    return " ".join(reversed(ls))


s = "the sky is blue"
print(reverse_word(s))
