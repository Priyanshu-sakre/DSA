from typing import List
from collections import deque


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        bfs = []
        visited = [0] * len(adj)
        queue = deque()
        queue.append(0)
        visited[0] = 1
        self.bfs(adj, bfs, queue, visited)
        return bfs

    def bfs(self, adj, bfs, queue, visited):
        while queue:
            e = queue.popleft()
            bfs.append(e)
            for i in adj[e]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
