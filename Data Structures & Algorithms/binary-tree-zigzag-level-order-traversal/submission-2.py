# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([root])
        left_to_right = True

        res = []

        if not root:
            return []

        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            if not left_to_right:
                level.reverse()
            res.append(level)
            left_to_right = not left_to_right

                
        return res
        