# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution: #短い　44ms
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

class Solution: #長い 36ms
    def maxDepth(self, root: TreeNode) -> int:
        self.d = deque()
        # print(root)
        self.d.append((root, 0))
        if root == None:
            return 0
        result = self.dfs(self.d, 0)
        # print(result)
        return result

    def dfs(self, d, max_depth):
        if d == deque():
            return max_depth
        tup = d.pop()
        # print(tup)
        tree = tup[0]
        depth = tup[1]+1
        if max_depth < depth:
            max_depth = depth
        val = tree.val
        left = tree.left
        if left:
            d.append((left, depth))
        right = tree.right
        if right:
            d.append((right, depth))

        return self.dfs(d,max_depth)
