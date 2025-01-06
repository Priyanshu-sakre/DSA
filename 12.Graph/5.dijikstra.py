from typing import List, Tuple
import heapq


class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        V = len(adj)  # Number of vertices
        dist = [float("inf")] * V  # Distance array initialized to infinity
        dist[src] = 0  # Distance to source is 0

        # Min-heap to store (distance, vertex)
        heap = [(0, src)]

        while heap:
            d, u = heapq.heappop(heap)

            # Process all adjacent vertices of the current vertex
            for v, weight in adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(heap, (dist[v], v))

        return dist
