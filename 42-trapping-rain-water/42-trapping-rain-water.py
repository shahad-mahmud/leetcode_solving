class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        left_max=[0 for _ in range(len(height))]
        right_max=[0 for _ in range(len(height))]
        
        j=len(height)-1
        for i in range(1, len(height)):
            left_max[i]=max(left_max[i-1], height[i-1])
            right_max[j-i]=max(right_max[j-i+1], height[j-i+1])
        
        
        for i in range(len(height)):
            water = min(left_max[i], right_max[i])-height[i]
            res += water if water>0 else 0
        
        return res