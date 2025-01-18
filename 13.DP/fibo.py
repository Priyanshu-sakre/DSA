class Solution:
    MOD = 10**9 + 7

    def topDown(self, n):
        dp = [-1] * (n + 1)  # Initialize dp array with -1

        def dp1(dp, n):
            if n <= 1:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] = (dp1(dp, n - 1) + dp1(dp, n - 2)) % Solution.MOD
            return dp[n]

        return dp1(dp, n)

    def bottomUp(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            curr = (b + a) % Solution.MOD
            a = b
            b = curr
        return b
