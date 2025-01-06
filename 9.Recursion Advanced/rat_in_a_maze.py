class Solution:
    # Function to find all possible paths
    def solve(self, i, j, n, ans, vis, move):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        # down
        if i + 1 < n and not vis[i + 1][j] and mat[i + 1][j] == 1:
            vis[i][j] = 1
            self.solve(i + 1, j, n, ans, vis, move + "D")
            vis[i][j] = 0
        # left
        if j - 1 >= 0 and not vis[i][j - 1] and mat[i][j - 1] == 1:
            vis[i][j] = 1
            self.solve(i, j - 1, n, ans, vis, move + "L")
            vis[i][j] = 0
        # right
        if j + 1 < n and not vis[i][j + 1] and mat[i][j + 1] == 1:
            vis[i][j] = 1
            self.solve(i, j + 1, n, ans, vis, move + "R")
            vis[i][j] = 0
        # up
        if i - 1 >= 0 and not vis[i - 1][j] and mat[i - 1][j] == 1:
            vis[i][j] = 1
            self.solve(i - 1, j, n, ans, vis, move + "U")
            vis[i][j] = 0

    def findPath(self, mat):
        n = len(mat)
        ans = []
        vis = [[0] * n for _ in range(n)]
        if mat[0][0] == 1:
            self.solve(0, 0, n, ans, vis, "")
        return ans
