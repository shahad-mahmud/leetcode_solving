# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root)
    
    def dfs(self, node, max_val=-10009):
        count=0
        if node.val>=max_val:
            count=1
            max_val=node.val
        
        if node.left: count += self.dfs(node.left, max_val)
        if node.right: count +=  self.dfs(node.right, max_val)
        
        return count