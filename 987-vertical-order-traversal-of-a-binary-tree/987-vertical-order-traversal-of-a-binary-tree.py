# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_, max_=0, 0
        
        q=deque([(root, 0)])
        while q:
            head, i=q.popleft()
            if i<min_: min_=i
            if i>max_: max_=i
            
            if head.left:
                q.append((head.left, i-1))
            if head.right:
                q.append((head.right, i+1))
        
        res_size=max_-min_+1
        res=[[] for _ in range(res_size)]
        lev=[[] for _ in range(res_size)]
        min_abs=abs(min_)
        prev_lev=0
        
        q=deque([(root, 0, 0)])
        while q:
            head, l, i=q.popleft()
            
            if l!=prev_lev:
                for j in range(res_size):
                    res[j].extend(list(sorted(lev[j])))
                    lev[j]=[]
                prev_lev=l
            
            lev[i+min_abs].append(head.val)
            
            if head.left:
                q.append((head.left, l+1, i-1))
            if head.right:
                max_+=1
                q.append((head.right, l+1, i+1))
        
        for j in range(res_size):
            res[j].extend(list(sorted(lev[j])))
            lev[j]=[]
        
        return res