# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        s, n_nodes = root.val, 1
        res=[]
        
        q=deque([(root, 0)])
        prev_level=0
        
        while q:
            head, l=q.popleft()
            
            if l!=prev_level:
                res.append(s/n_nodes) 
                s,n_nodes=0,0
                
            s+=head.val
            n_nodes+=1
            
            prev_level=l
            
            if head.left: q.append((head.left, l+1))
            if head.right: q.append((head.right, l+1))
        
        if n_nodes>0:
            res.append(s/n_nodes) 
        
        return res