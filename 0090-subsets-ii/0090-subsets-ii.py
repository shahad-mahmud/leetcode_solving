class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums, self.res = nums, []
        self.nums.sort()
        self.get_res([], 0)
        return self.res
    
    def get_res(self, res, pos):
        if pos >= len(self.nums):
            self.res.append(res)
            return
        
        self.get_res(res+[self.nums[pos]], pos+1)
        
        while pos+1 < len(self.nums) and self.nums[pos] == self.nums[pos+1]:
            pos+=1
        
        self.get_res(res, pos+1)