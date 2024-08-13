n = 153
num = n
arm_num = 0
l1 = len(str(num))
while num != 0:
    a = num % 10
    arm_num += a**l1
    num //= 10
if n == arm_num:
    print("Armstrong Number")
else:
    print("Not an Armtrong Number")
