class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens=sorted(tokens)
        l,r=0, len(tokens)-1
        s, fs=0, 0
        
        while l<=r:
            if tokens[l]<=power:
                s+=1
                power-=tokens[l]
                l+=1
                fs=max(fs,s)
            elif power < tokens[l] and s>0:
                s-=1
                power+=tokens[r]
                r-=1
            else:
                break
        
        return fs
        