# brute
# better
# same as n/2


# optimal
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        ele1 = 0
        ele2 = 0
        for i in range(len(nums)):
            if count1 == 0 and nums[i] != ele2:
                count1 = 1
                ele1 = nums[i]
            elif count2 == 0 and nums[i] != ele1:
                count2 = 1
                ele2 = nums[i]
            elif ele1 == nums[i]:
                count1 += 1
            elif ele2 == nums[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        list1 = []
        count1 = 0
        count2 = 0
        for i in nums:
            if i == ele1:
                count1 += 1
            if i == ele2:
                count2 += 1
        if count1 > len(nums) // 3:
            list1.append(ele1)
        if count2 > len(nums) // 3 and ele2 not in list1:
            list1.append(ele2)
        return list1
