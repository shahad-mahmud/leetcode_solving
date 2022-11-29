class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        self.get_subsets(0, [])
        
        return self.result
    
    def get_subsets(self, cur_pos, res):
        if cur_pos > len(self.nums):
            return
        
        self.result.append(res)
        
        for i in range(cur_pos, len(self.nums)):
            self.get_subsets(i+1, res+[self.nums[i]])