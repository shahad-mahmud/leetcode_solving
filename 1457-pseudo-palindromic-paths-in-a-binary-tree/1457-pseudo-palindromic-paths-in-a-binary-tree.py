# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    frq=defaultdict(int)
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res=0
        
        stack=[(root, 0)]
        while stack:
            node, path=stack.pop()
            if node is not None:
                path ^= 1<<node.val
                
                if node.left is None and node.right is None:
                    if path & (path-1)==0:
                        res+=1
                else:
                    stack.append((node.left, path))
                    stack.append((node.right, path))
        
        return res