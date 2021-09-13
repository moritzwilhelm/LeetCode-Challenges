import heapq
from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt

        res = 0
        pq = [(0, 0)]
        dist = {0: 0}
        subdivided = {}

        while len(pq):
            distance, node = heapq.heappop(pq)
            if distance > dist[node]:
                continue

            # we only visit each node of the original graph once via the shortest path to it
            # (due to non-negative weights)
            res += 1
            remaining_moves = maxMoves - distance

            for neighbor, cnt in graph[node].items():
                subdivided[(node, neighbor)] = min(cnt, remaining_moves)

                # shortest path to current node + 1 hop per new node + 1 hop to actual neighbor
                new_distance = distance + cnt + 1
                if new_distance < dist.get(neighbor, maxMoves + 1):
                    dist[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

        for u, v, cnt in edges:
            res += min(cnt, subdivided.get((u, v), 0) + subdivided.get((v, u), 0))

        return res
