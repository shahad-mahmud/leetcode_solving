class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        score = zip(efficiency, speed)
        score = sorted(score, key=lambda x: x[0], reverse=True)
        
        temp, res=0, 0
        heap=[]
        
        for e, s in score:
            heapq.heappush(heap, s)
            temp+=s
            
            if len(heap)>k:
                temp-=heapq.heappop(heap)
            
            res=max(res, temp*e)
        
        return res%1000000007
        