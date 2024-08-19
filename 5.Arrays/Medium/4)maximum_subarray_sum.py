# brute
def maxSubArray(nums):
    sum_final = nums[0]
    for i in range(len(nums)):
        sum2 = 0
        for j in range(i, len(nums)):
            sum2 += nums[j]
            sum_final = max(sum2, sum_final)
    return sum_final


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))
# optimal
"""Kadane's Algorithm"""


def maxSubArray2(nums):
    sum1 = 0
    max1 = nums[0]
    for i in nums:
        sum1 += i
        max1 = max(max1, sum1)
        if sum1 < 0:
            sum1 = 0
    return max1


print(maxSubArray2(nums))
