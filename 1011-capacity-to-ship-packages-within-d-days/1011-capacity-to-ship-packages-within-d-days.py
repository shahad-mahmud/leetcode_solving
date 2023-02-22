class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        self.w = weights
        self.d = days
        
        while l<r:
            m = (l+r)//2
            
            if self.is_possible(m):
                r=m
            else:
                l=m+1
        
        return l
    
    def is_possible(self, cap):
        s = 0
        d = 1
        
        for w in self.w:
            s += w
            
            if s>cap:
                d+=1
                s=w
            
            if d>self.d:
                return False
        
        return True