# brute
def majorityElement(nums):
    for i in nums:
        count = 0
        for j in nums:
            if i == j:
                count += 1
        if count > len(nums) // 2:
            return i


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))


# better
def majorityElement2(nums):
    hash_map = {}
    for i in nums:
        hash_map[i] = hash_map.get(i, 0) + 1
    for i in hash_map:
        if hash_map[i] > len(nums) // 2:
            return i


print(majorityElement2(nums))


# optimal
"""Moore's Voting Algorithm"""


def majorityElement3(nums):
    count = 0
    for i in range(len(nums)):
        if count == 0:
            count = 1
            el = nums[i]
        elif nums[i] == el:
            count += 1
        else:
            count -= 1
    count1 = 0
    for i in range(len(nums)):
        if nums[i] == el:
            count1 += 1
    if count1 > len(nums) // 2:
        return el
    return -1


print(majorityElement3(nums))
# optimal 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        el = 0
        for i in range(len(nums)):
            if count == 0:
                el = nums[i]
            if nums[i] == el:
                count += 1
            else:
                count -= 1
        return el
