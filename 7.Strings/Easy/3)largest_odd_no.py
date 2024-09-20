def largest_odd_no(num):
    s = ""
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[0 : i + 1]
    return s


num = "35427"
print(largest_odd_no(num))
