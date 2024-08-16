# brute
nums = [4, 1, 2, 1, 2]
for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count += 1
    if count == 1:
        print(i)

# better

"""
if only positives->use list hashing
if negatives also->use dict hashing
"""

# optimal

xor1 = 0
for i in nums:
    xor1 = xor1 ^ i
print(xor1)
