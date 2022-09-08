class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        res=[]
        lp, rp=0, 0
        
        while rp < len(nums):            
            while dq and nums[dq[-1]] < nums[rp]:
                dq.pop()
            dq.append(rp)
            
            if dq[0] < lp:
                dq.popleft()
            
            if rp - lp + 1 == k:
                res.append(nums[dq[0]])
                lp+=1
            
            rp+=1
        
        return res
                