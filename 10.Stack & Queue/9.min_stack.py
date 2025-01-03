# 1st approach
# using 2 stacks
class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        self.minn = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini or val <= self.mini[-1]:
            self.mini.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # Only pop from mini if the popped value matches the top of mini.
            if self.mini and val == self.mini[-1]:
                self.mini.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.mini:
            return -1
        return self.mini[-1]


# 2nd approach
# using mini
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            mini = min(val, self.stack[-1][-1])
            self.stack.append([val, mini])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]
