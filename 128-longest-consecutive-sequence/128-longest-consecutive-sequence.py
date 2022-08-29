class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=defaultdict(int)
        longest_seq=defaultdict(int)
        
        for n in nums:
            m[n]+=1
        
        res=0
        for n in nums:
            l=1
            i=n+1
            while m[i]>0:
                if longest_seq[i]>0:
                    l+=longest_seq[i]
                    break
                l+=1
                i+=1
            longest_seq[n]=l
            res=max(res, l)
        return res
        