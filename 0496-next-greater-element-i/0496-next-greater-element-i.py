class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_ids = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                top = stack.pop()
                index = n1_ids[top]
                
                res[index] = n
        
            if n in n1_ids:
                stack.append(n)
        
        return res
        