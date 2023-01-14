class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        x, y = intervals[0][0], intervals[0][1]
        res = []
        
        for i, j in intervals:
            if y < i:
                res.append([x, y])
                x, y = i, j
            else:
                x = min(x, i)
                y = max(y, j)
        
        res.append([x, y])
        return res
        