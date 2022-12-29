class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # build the graph
        graph = {node:[] for node in range(n)}  # [i, cost]
        
        for i, (x, y) in enumerate(points):
            for j, (a, b) in enumerate(points):
                dis = abs(x-a) + abs(y-b)
                graph[i].append((j, dis))
        
        
        # find MST
        visited = set()
        q = [(0,0)]
        
        total_cost = 0
        
        while q:
            # print(len(visited), n)
            if len(visited) == n: break
                
            # print(q)
            cost, node = heapq.heappop(q)
            while node in visited and q:
                cost, node = heapq.heappop(q)
            
            # print(cost, node, visited, q)
            # print()
            
            total_cost += cost
            visited.add(node)
            
            for child in graph[node]:
                # print(child)
                if child[0] not in visited:
                    heapq.heappush(q, (child[1], child[0]))
                # print(q)
        
        return total_cost