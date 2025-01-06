class Solution:
    def count(self, n):
        # Code here
        return 2 ** (n * (n - 1) // 2)
