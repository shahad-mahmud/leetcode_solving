class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        prev = intervals[0][1]
        
        for i, (x, y) in enumerate(intervals[1:]):
            if x>=prev:
                prev = y
            else:
                res += 1
                prev = min(y, prev)
        
        return res