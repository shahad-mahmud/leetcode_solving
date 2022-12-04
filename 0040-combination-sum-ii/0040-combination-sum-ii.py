class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtract(pos, s, res):            
            if s==target:
                result.append(res.copy())
            elif s>target:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev: continue
                
                res.append(candidates[i])
                backtract(i+1, s+candidates[i], res)
                res.pop()
                prev = candidates[i]
        
        backtract(0,0,[])
        return result