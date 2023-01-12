class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        
        for i, c in enumerate(s):
            last_index[c] = i
        
        end = last_index[s[0]]
        start = 0
        res = []
        for i, c in enumerate(s):
            if last_index[c] > end:
                end = last_index[c]
            if i == end:
                res.append(end-start+1)
                start = i+1
        
        return res