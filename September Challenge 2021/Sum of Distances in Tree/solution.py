from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.subtree_size = []
        self.result = []
        self.successors = defaultdict(set)

    def precompute(self, root, predecessor):
        """precomputes the number of nodes in the subtree rooted at each node of the graph & sum of distances of nodes in current subtree"""
        for successor in self.successors[root]:
            if successor != predecessor:
                self.precompute(successor, root)
                # number of nodes in current subtree is equal to sum of nodes in each successor's subtree
                self.subtree_size[root] += self.subtree_size[successor]
                # depth increases by 1 -> result increases by n * 1
                self.result[root] += self.result[successor] + self.subtree_size[successor]

    def update_results(self, root, predecessor):
        """update sum of distances recursively by computing change to predecessor's result"""
        for successor in self.successors[root]:
            if successor != predecessor:
                # depth of all nodes in current subtree decreases by 1 (-> - self.subtree_size[successor] * 1) and
                # depth of all other nodes increases by 1 (-> + (n - self.subtree_size[successor]) * 1)
                self.result[successor] = self.result[root] + (len(self.result) - self.subtree_size[successor]) \
                                         - self.subtree_size[successor]
                self.update_results(successor, root)

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """computes sum of distances of a node by summing up the depth of each other node by performing one post-order traversal followed by one pre-oder traversal"""
        self.subtree_size += [1] * n
        self.result += [0] * n

        for a, b in edges:
            self.successors[a].add(b)
            self.successors[b].add(a)

        self.precompute(0, -1)  # post-order traversal
        self.update_results(0, -1)  # pre-oder traversal

        return self.result
