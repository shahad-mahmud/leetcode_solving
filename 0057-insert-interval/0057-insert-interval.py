class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        x, y = newInterval
        
        for idx, (i, j) in enumerate(intervals):
            if y < i:
                res.append([x,y])
                return res + intervals[idx:]
            elif j < x:
                res.append([i,j])
            else:
                x = min(x, i)
                y = max(y, j)
        
        res.append([x, y])
        return res
        