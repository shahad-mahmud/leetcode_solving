class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        
        m=defaultdict(lambda:-1)
        
        length=0
        lp, rp=0, 0
        
        while rp<len(s):
            if m[s[rp]]>=0 and m[s[rp]]>=lp:
                if rp-lp>length:
                    length=rp-lp
                
                lp=m[s[rp]]+1
            
            m[s[rp]]=rp
            rp+=1
        
        if rp-lp>length:
            length=rp-lp
        
        return length