# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        l, r="", ""
        
        if root.left:
            l= f"({self.tree2str(root.left)})"
        if root.right:
            r= f"({self.tree2str(root.right)})"
        
        if root.left is None and root.right is not None:
            return str(root.val) + "()" + r
        
        return str(root.val) + l + r