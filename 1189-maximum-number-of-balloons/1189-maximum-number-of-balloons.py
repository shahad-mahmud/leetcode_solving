class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {c: 0 for c in "balloon"}
        
        for c in text:
            if c in counter:
                counter[c] += 1
        
        res = 0
        while True:
            for c in "balloon":
                if not counter[c]:
                    return res
                counter[c] -= 1
            res += 1
        
        return res