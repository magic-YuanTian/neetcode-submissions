# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode()

        preorder[0]

        def dfs(node, pre_temp, in_temp):

            root_val = pre_temp[0]
            node.val = root_val

            in_root_idx = in_temp.index(root_val)

            left_in = in_temp[:in_root_idx]
            right_in = in_temp[in_root_idx+1:]

            left_pre = pre_temp[1:in_root_idx+1]
            right_pre = pre_temp[in_root_idx+1:]
            
            if len(left_pre) > 0:
                left_node = TreeNode()
                node.left = dfs(left_node, left_pre, left_in)

            if len(right_pre) > 0:
                right_node = TreeNode()
                node.right = dfs(right_node, right_pre, right_in)

            return node



        dfs(root, preorder, inorder)


        return root