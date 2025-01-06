from typing import List


class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize the adjacency list with empty lists for each node
        adj_list = [[] for _ in range(V)]

        # Fill the adjacency list
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Return the adjacency list
        return adj_list
