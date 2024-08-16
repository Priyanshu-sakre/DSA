nums = [1, 1, 0, 1, 1, 1]


def counter(nums):
    count = 0
    maxx = 0
    for i in nums:
        if i == 1:
            count += 1
            if count > maxx:
                maxx += 1  # or maxx=max(count,maxx)
        else:
            count = 0
    return maxx


print(counter(nums))
