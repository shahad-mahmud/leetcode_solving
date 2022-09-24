# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        
        self.res=[]
        self.psum(root, targetSum, 0, [])
        
        return self.res
    
    def psum(self, node, t, s, p):     
        s+=node.val
        
        if node.left:
            self.psum(node.left, t, s, p+[node.val])
        if node.right:
            self.psum(node.right, t, s, p+[node.val])
            
        if node.left is None and node.right is None and s==t:
            self.res.append(p+[node.val])