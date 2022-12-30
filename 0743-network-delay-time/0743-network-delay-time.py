class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)  # key: source -> value: tuple(weight, destination)
        for u, v, w in times:
            graph[u].append((w, v))
        
        visited = set()
        q = [(0, k)]  # (cost, node)
        cost = 0
        
        while q:
            if len(visited) == n:
                break
            
            cost, node = heapq.heappop(q)
            visited.add(node)
            
            for w, d in graph[node]:
                if d not in visited:
                    heapq.heappush(q, (cost+w, d))
        
        return cost if len(visited)==n else -1
                