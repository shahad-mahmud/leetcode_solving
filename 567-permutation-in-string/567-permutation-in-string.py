class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1, c2 = defaultdict(int), defaultdict(int)
        
        for c in s1:
            c1[c]+=1
        
        l, r = 0, 0
        
        while r < len(s2):
            if r-l+1 <= len(s1):
                c2[s2[r]]+=1
            else:
                if self.is_equal(c1, c2):
                    return True
                
                c2[s2[l]]-=1
                l+=1
                
                c2[s2[r]]+=1
            
            r+=1
        
        if self.is_equal(c1, c2):
            return True
        
        return False
                
    def is_equal(self, c1, c2):
        for f in c1:
            if not c1[f]==c2[f]:
                return False
        return True
        
        