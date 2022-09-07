class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m=defaultdict(lambda:0)
        
        l,r=0,0
        mf=0  # max frequency
        ml=0
        
        while r<len(s):
            m[s[r]]+=1
            
            if m[s[r]]>mf:
                mf=m[s[r]]
            
            if (r-l+1)-mf <= k:
                if r-l+1>ml:
                    ml=r-l+1
            else:
                m[s[l]]-=1
                l+=1
                mf=0
            
            r+=1
        
        return ml