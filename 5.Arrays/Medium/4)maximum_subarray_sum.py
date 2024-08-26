# brute
def maxSubArray(nums):
    sum_final = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum1 = 0
            for k in range(i, j + 1):
                sum1 += nums[k]
                sum_final = max(sum1, sum_final)
    return sum_final


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))


# better


def maxSubArray2(nums):
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


def maxSubArray3(nums):
    sum1 = 0
    max1 = nums[0]
    for i in nums:
        sum1 += i
        # max1 = max(max1, sum1) (either of them can be used)
        if sum1 > max1:
            max1 = sum1
        if sum1 < 0:
            sum1 = 0
    return max1


print(maxSubArray3(nums))


# follow up question to print the sub-array
def maxSubArray4(nums):
    sum1 = 0
    max1 = nums[0]
    ans_s = 0
    ans_e = 0
    for i in range(len(nums)):
        if sum1 == 0:
            start = i
        sum1 += nums[i]
        # max1 = max(max1, sum1) (either of them can be used)
        if sum1 > max1:
            max1 = sum1
            ans_s = start
            ans_e = i
        if sum1 < 0:
            sum1 = 0
    for i in range(ans_s, ans_e + 1):
        print(nums[i], end=" ")
    print(nums[ans_s : ans_e + 1])
    # any on the above


maxSubArray4(nums)
