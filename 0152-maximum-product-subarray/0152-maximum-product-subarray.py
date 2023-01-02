class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        
        max_prod, min_prod = 1, 1
        
        for n in nums:
            temp = max_prod * n
            max_prod = max(temp, min_prod * n, n)
            min_prod = min(temp, min_prod * n, n)
            
            res = max(res, max_prod)
        
        return res
        
        
        