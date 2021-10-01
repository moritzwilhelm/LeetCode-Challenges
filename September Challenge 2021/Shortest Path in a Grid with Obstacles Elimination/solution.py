from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        # check if we can take the shortest path independently of the grid (by breaking any obstacle)
        if k >= m + n - 3:
            return m + n - 2

        visited = {(0, 0, k)}
        q = deque([(0, 0, k, 0)])

        while q:
            x, y, k, steps = q.popleft()

            if (x, y) == (m - 1, n - 1):
                return steps

            for x_, y_ in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                if 0 <= x_ < m and 0 <= y_ < n and k >= grid[x_][y_]:
                    neighbor = (x_, y_, k - grid[x_][y_])
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor + (steps + 1,))
        return -1
