num = 97
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count > 2:
    print("Not Prime")
if count == 2:
    print("Prime")
