class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        a = []
        index = 0
        self.solve(ans, a, nums, index)
        return ans

    def solve(self, ans, a, nums, index):
        if index == len(nums):
            ans.append(a.copy())
            return

        a.append(nums[index])
        self.solve(ans, a, nums, index + 1)
        a.pop()

        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1

        self.solve(ans, a, nums, index + 1)
