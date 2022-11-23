class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        info = defaultdict(int)
        for t in tasks:
            info[t]+=1
        
        counts = [-v for v in info.values()]
        heapq.heapify(counts)
        
        q = deque([])
        res, time = 0, 0
        
        while counts or q:
            res +=1
            time += 1
            
            if counts:
                t = heapq.heappop(counts)
                t += 1
                if t<0:
                    q.append((t,time+n))
            
            if q and q[0][1] <= time:
                t = q.popleft()[0]
                heapq.heappush(counts, t)
        
        return res
        
            