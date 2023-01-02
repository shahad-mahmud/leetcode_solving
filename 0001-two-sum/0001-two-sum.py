class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {k:v for v,k in enumerate(nums)}
        
        for i, num in enumerate(nums):
            t = target-num
            if t in map_ and map_[t] != i:
                return [i, map_[t]]
        return []
        