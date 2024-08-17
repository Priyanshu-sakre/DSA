# brute
"""
use any sorting algo say merge sort
"""


# better
def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in nums:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1
    for j in range(count_0):
        nums[j] = 0
    for k in range(count_0, count_0 + count_1):
        nums[k] = 1
    for l in range(count_0 + count_1, len(nums)):
        nums[l] = 2
    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
