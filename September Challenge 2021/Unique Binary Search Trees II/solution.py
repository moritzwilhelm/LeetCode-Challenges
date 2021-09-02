from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTreesRecursive(self, start, end, tree_cache):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        if (start, end) in tree_cache:
            return tree_cache[(start, end)]

        trees = []
        for i in range(start, end + 1):
            left_subtrees = self.generateTreesRecursive(start, i - 1, tree_cache)
            right_subtrees = self.generateTreesRecursive(i + 1, end, tree_cache)

            for left in left_subtrees:
                for right in right_subtrees:
                    trees.append(TreeNode(i, left, right))

        tree_cache[(start, end)] = trees
        return trees

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        tree_cache = {}
        return self.generateTreesRecursive(1, n, tree_cache)
