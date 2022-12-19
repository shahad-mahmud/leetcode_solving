class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        
        for i in range(l):
            nums.append(nums[i])
        
        return nums
        