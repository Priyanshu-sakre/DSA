class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        visited = [0] * len(adj)
        start = 0
        ans = []

        def dfs(visited, start, ans):
            visited[start] = 1
            ans.append(start)
            for i in adj[start]:
                if visited[i] == 0:
                    dfs(visited, i, ans)
                    visited[i] = 1

        dfs(visited, start, ans)
        return ans
