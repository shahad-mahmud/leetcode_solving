class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, h, m = 0, len(nums)-1, 0
        
        while m<=h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l+=1
                m+=1
            elif nums[m]==2:
                nums[h], nums[m] = nums[m], nums[h]
                h-=1
            else:
                m+=1
                
        