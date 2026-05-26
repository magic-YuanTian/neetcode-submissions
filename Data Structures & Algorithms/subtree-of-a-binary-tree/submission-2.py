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
            # 前面没 return，说明至少有一个存在。如果此时有一个为 None，必不匹配
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
                
            # 直接返回左右子树的布尔值求值结果
            return same(node1.left, node2.left) and same(node1.right, node2.right)

        # 直接复用外层的函数作为 dfs 递归，不需要额外写一个 dfs 内部函数
        if not root:
            return False
            
        # 先查当前节点
        if same(root, subRoot):
            return True
            
        # 当前不行，再去左右子树里找
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        

