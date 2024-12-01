# brute
class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum1 = 1
        for i in range(1, n + 1):
            sum1 *= i
        rs = 0
        while sum1 % 10 == 0:
            rs += 1
            sum1 = sum1 // 10
        return rs


# better
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        i = 5
        while i <= n:
            res += n // i
            i *= 5
        return res
