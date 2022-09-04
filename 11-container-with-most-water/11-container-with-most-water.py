class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        
        while l<r:
            water=(r-l)*min(height[l], height[r])
            
            if water>res: res=water
            
            if height[l] > height[r]:
                r-=1
            elif height[l] < height[r]:
                l+=1
            else:
                l+=1
                r-=1
        
        return res