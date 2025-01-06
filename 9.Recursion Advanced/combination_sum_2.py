from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort to handle duplicates and make the recursion efficient

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the current candidate is greater than the remaining target, break early
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result
 