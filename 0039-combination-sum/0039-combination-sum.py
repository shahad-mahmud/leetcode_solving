class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cs, self.tg = candidates, target
        self.res = []
        
        self.get_comb(0,0,[])
        return self.res
    
    def get_comb(self, pos, s, arr):
        if pos > len(self.cs) or s > self.tg:
            return
        
        if s==self.tg:
            self.res.append(arr)
        
        for i in range(pos, len(self.cs)):
            self.get_comb(i, s+self.cs[i], arr+[self.cs[i]])
        