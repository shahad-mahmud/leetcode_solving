class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        
        for n in nums:
            if n-1 not in s:
                c = 0
                while n in s:
                    n+=1
                    c+=1
                if c > res:
                    res = c
        
        return res
        