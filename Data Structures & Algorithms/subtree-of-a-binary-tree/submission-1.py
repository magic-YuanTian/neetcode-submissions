# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def same(node1, node2):

            if not node1 and not node2:
                return True
            elif (not node1 and node2) or (not node2 and node1):
                return False

            if not node1.val == node2.val:
                return False

            if same(node1.left, node2.left) and same(node1.right, node2.right):
                return True
            else:
                return False

        def dfs(node):

            if not node:
                if not subRoot:
                    return True
                else:
                    return False
            
            if same(node.right, subRoot) or same(node.left, subRoot):
                return True

            return dfs(node.right) or dfs(node.left)

        return same(root, subRoot) or dfs(root)

        

