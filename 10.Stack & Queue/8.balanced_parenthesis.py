class Solution:
    def isValid(self, s: str) -> bool:
        # optimization
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if (
                    (i == ")" and stack[-1] == "(")
                    or (i == "}" and stack[-1] == "{")
                    or (i == "]" and stack[-1] == "[")
                ):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
