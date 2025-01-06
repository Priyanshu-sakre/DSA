class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(ans, subs, index):
            if index == len(s):
                ans.append(subs.copy())
                return
            for i in range(index, len(s)):
                if self.palindrome(s, index, i):
                    subs.append(s[index : i + 1])
                    backtrack(ans, subs, i + 1)
                    subs.pop()

        ans = []
        a = []
        index = 0
        backtrack(ans, a, index)
        return ans

    def palindrome(self, string, start, end):
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True
