class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.per([], set())
        return self.res
    
    def per(self, res, visited):
        if len(res) >= len(self.nums): 
            self.res.append(res)
            return
        
        for i in range(0, len(self.nums)):
            if i not in visited:
                self.per(res+[self.nums[i]], visited.union({i}))
        