class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cs, ct = defaultdict(int), defaultdict(int)
        
        for c in t:
            ct[c]+=1
        
        lp, rp = 0, 0
        res=""
        min_len=100009
        
        while rp<len(s):
            cs[s[rp]]+=1
            
            if self.is_equal(ct, cs):
                while self.is_equal(ct, cs) and lp<=rp:
                    cs[s[lp]]-=1
                    lp+=1
                
                if rp - lp - 1 < min_len:
                    res=s[lp-1:rp+1]
                    min_len=rp-lp-1
            
            rp+=1
        
        return res
    
    def is_equal(self, c1, c2):
        for f in c1:
            if not c1[f]<=c2[f]:
                return False
        return True
        