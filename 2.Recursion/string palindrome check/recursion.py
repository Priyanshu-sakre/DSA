def check_palindrome(i, s):
    l1 = len(s)
    if i >= l1 // 2:
        return True
    if s[i] != s[l1 - i - 1]:
        return False
    return check_palindrome(i + 1, s)


s = "MADAM"
print(check_palindrome(0, s))
