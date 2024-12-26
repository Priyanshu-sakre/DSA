class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        pref[0] = 1
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]
        suff = [0] * len(nums)
        suff[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        list1 = [0] * len(nums)
        for i in range(len(pref)):
            list1[i] = pref[i] * suff[i]
        return list1
