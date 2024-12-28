# for strings
def all_subsets(n, curr="", i=0):
    if i == len(n):
        print(f"'{curr}'", end=" ")
        return
    all_subsets(n, curr, i + 1)
    all_subsets(n, curr + n[i], i + 1)


n = "ABC"
all_subsets(n)
# for arrays
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        a = []
        index = 0
        self.solve(ans, a, nums, index)
        return ans

    def solve(self, ans, a, nums, index):
        if index == len(nums):
            ans.append(a.copy())
            return
        self.solve(ans, a, nums, index + 1)
        a.append(nums[index])
        self.solve(ans, a, nums, index + 1)
        a.pop()
