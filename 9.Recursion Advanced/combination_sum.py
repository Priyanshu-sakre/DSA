class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        index = 0
        a = []
        self.comb(a, ans, index, candidates, target)
        return ans

    def comb(self, a, ans, index, candidates, target):
        if target == 0:
            ans.append(a.copy())
            return
        if index >= len(candidates):
            return
        if candidates[index] <= target:
            a.append(candidates[index])
            target -= candidates[index]
            self.comb(a, ans, index, candidates, target)
            a.pop()
            target += candidates[index]
        self.comb(a, ans, index + 1, candidates, target)
