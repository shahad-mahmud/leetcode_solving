class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        
        lp, rp=0, len(height)-1
        left_max, right_max=height[lp],height[rp]
        
        while lp<rp:             
            if left_max<=right_max:
                lp+=1
                left_max=max(left_max, height[lp])
                
                water = left_max-height[lp]
                res += water if water>0 else 0
            else:
                rp-=1
                right_max=max(right_max, height[rp])
                
                water = right_max-height[rp]
                res += water if water>0 else 0                
        
        return res