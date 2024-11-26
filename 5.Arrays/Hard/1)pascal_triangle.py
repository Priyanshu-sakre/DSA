# type 1
n = 5
r = 3


def ncr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    print(res)


ncr(n - 1, r - 1)

# type 2


def printer(n):
    for i in range(1, n + 1):
        print(ncr(n - 1, i - 1), end=" ")


def ncr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


n = 5
printer(n)
ncr(n - 1, r - 1)


# type 3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l1 = []
        for i in range(0, numRows):
            l = []
            for j in range(i + 1):
                l.append(self.ncr(i, j))
            l1.append(l)
        return l1

    def ncr(self, n, r):
        res = 1
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        return res
