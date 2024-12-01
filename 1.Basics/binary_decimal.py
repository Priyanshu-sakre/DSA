s = "10001"


def decimal(s):
    dec = 0
    power = 0
    for i in range(len(s) - 1, -1, -1):
        dec = dec + (int(s[i]) * (2**power))
        power += 1
    return dec


print(decimal(s))
