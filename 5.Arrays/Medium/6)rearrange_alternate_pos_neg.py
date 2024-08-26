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
    for i in range(len(neg)):
        nums[i * 2] = pos[i]
        nums[(i * 2) + 1] = neg[i]
    return nums


nums = [3, 1, -2, -5, 2, -4]
print(rearrangeArray(nums))


# optimal (if positives==negatives)
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


# variety 2 (if positives!=negatives)
def rearrangeArray3(nums1: List[int]) -> List[int]:
    pos = []
    neg = []
    for i in nums1:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    n = len(pos)
    m = len(neg)
    for i in range(min(n, m)):
        nums1[i * 2] = pos[i]
        nums1[i * 2 + 1] = neg[i]
    index = min(n, m) * 2
    for i in range(index, len(nums1)):
        if n > m:
            nums1[i] = pos[i - m]
        else:
            nums1[i] = neg[i - n]
    return nums1


nums1 = [3, -2, 1, -5, 2, -4, 7, 8, 9, -7, -8]
print(rearrangeArray3(nums1))
