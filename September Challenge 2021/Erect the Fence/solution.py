from typing import List


class Solution:
    def determinant(self, a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

    # implements (two-sided) Grahan Scan
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) < 4:
            return trees

        trees.sort()

        front_hull = [trees[0], trees[1]]
        idx = 2
        while idx < len(trees):
            current = trees[idx]
            if len(front_hull) == 1 or self.determinant(front_hull[-2], front_hull[-1], current) <= 0:
                front_hull.append(current)
                idx += 1
            else:
                front_hull.pop()

        back_hull = [trees[-1], trees[-2]]
        idx = len(trees) - 3
        while idx >= 0:
            current = trees[idx]
            if len(back_hull) == 1 or self.determinant(back_hull[-2], back_hull[-1], current) <= 0:
                back_hull.append(current)
                idx -= 1
            else:
                back_hull.pop()

        return front_hull + [tree for tree in back_hull if tree not in front_hull]
