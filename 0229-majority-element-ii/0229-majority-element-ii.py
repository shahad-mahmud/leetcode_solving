class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) / 3
        
        c = Counter(nums)
        res = []
        
        for k, v in c.items():
            if v>target:
                res.append(k)
        
        return res
        