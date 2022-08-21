class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_len, target_len = len(stamp), len(target)
        
        permutations = set()
        for i in range(stamp_len):
            for j in range(stamp_len-i):
                permutations.add('*' * i + stamp[i:stamp_len-j] + '*' * j)
        
        res = []
        temp_target = '*' * target_len
        while target != temp_target:
            found=False
            
            for i in range(target_len-stamp_len, -1, -1):
                if target[i:i+stamp_len] in permutations:
                    target=target[:i]+'*' * stamp_len + target[i+stamp_len:]
                    res.append(i)
                    found=True
            
            if not found:
                return []
        
        return res[::-1]
        
        
        