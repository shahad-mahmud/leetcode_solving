class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running_sum=0
        max_sum=-float('inf')
        fp=lp=0
        
        while(lp<len(nums)):            
            if lp-fp>=k:           
                if running_sum>max_sum:
                    max_sum=running_sum
                
                running_sum-=nums[fp]
                fp+=1
            
            running_sum+=nums[lp]
            lp+=1
            
        print(max_sum)
        if running_sum>max_sum:
            max_sum=running_sum
        
        return max_sum/min(k, len(nums))