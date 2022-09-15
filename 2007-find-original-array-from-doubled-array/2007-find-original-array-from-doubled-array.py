class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # count n zeros
        # count even frequencies 
        n_zeros=0
        evens=defaultdict(int)
        odds=[]
        
        for n in changed:
            if n==0:
                n_zeros+=1
            elif n%2==0:
                evens[n]+=1
            else:
                odds.append(n)
        
        res=[]
        if n_zeros%2:
            return []
        else:
            res=[0 for _ in range(n_zeros//2)]
            
        for n in odds:
            if evens[2*n]>0:
                evens[2*n]-=1
                res.append(n)
            else:
                return []
        
        sk=sorted(evens)
        for k in sk:
            if evens[k]>0:
                if evens[2*k]<=0:
                    return []
                
                while evens[k]>0 and evens[2*k]>0:
                    evens[2*k]-=1
                    evens[k]-=1
                    res.append(k)
        
        return res
                
        