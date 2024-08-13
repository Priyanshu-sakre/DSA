n = 1331
num = n
rev_num = 0
while num != 0:
    a = num % 10
    rev_num = rev_num * 10 + a
    num //= 10
if n == rev_num:
    print("Palindrome")
else:
    print("Not a Palindrome")
