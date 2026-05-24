# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return None

        cnt = 0
        res = None
        
        def dfs(node):
            
            nonlocal cnt, res

            if node.left:
                dfs(node.left)

            cnt += 1
            if cnt == k:
                res = node.val
                return
            if node.right:
                dfs(node.right)

        dfs(root)

        return res