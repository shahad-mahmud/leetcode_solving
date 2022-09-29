class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = [(abs(x - num), num) for num in arr]
        heapify(pq)
        ans = []
        
        while pq and len(ans) < k:
            ans.append(heappop(pq)[1])
        
        return sorted(ans)