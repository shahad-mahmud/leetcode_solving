class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        l=len(temps)
        res=[0 for _ in range(l)]
        s=[]
        
        for i in range(l):
            while s and temps[i]>temps[s[-1]]:
                j=s.pop()
                res[j]=i-j
            s.append(i)
        
        return res
        