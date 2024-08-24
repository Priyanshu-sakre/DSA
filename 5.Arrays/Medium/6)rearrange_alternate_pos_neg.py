# brute
from typing import List


def rearrangeArray(nums: List[int]) -> List[int]:
    pos = []
    neg = []
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    for i in range(len(pos)):
        nums[i * 2] = pos[i]
        nums[(i * 2) + 1] = neg[i]
    return nums


nums = [3, 1, -2, -5, 2, -4]
print(rearrangeArray(nums))


# optimal
def rearrangeArray2(nums: List[int]) -> List[int]:
    temp = [0] * len(nums)
    pos = 0
    neg = 1
    for i in nums:
        if i < 0:
            temp[neg] = i
            neg += 2
        else:
            temp[pos] = i
            pos += 2
    return temp


print(rearrangeArray2(nums))
