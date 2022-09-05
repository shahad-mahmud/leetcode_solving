"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        q=deque([(root,0)])
        prev=0
        res=[]
        temp=[]
        
        while q:
            head, l=q.popleft()
            
            if l!=prev:
                res.append(temp)
                temp=[]
                prev=l
            
            temp.append(head.val)
            
            for child in head.children:
                q.append((child, l+1))
        
        if len(temp)>0:
            res.append(temp)
        
        return res
            
        