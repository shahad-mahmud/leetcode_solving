class Solution:
    def canFinish(self, n_cources: int, prereqs: List[List[int]]) -> bool:
        graph = {c:set() for c in range(n_cources)}
        
        for req in prereqs:
            graph[req[0]].add(req[1])
        
        visited = set()
        
        def dfs(i):
            if i in visited:
                return False
            if len(graph[i])==0:
                return True
            
            visited.add(i)
            
            for c in graph[i]:
                if not dfs(c):
                    return False
            
            visited.remove(i)
            graph[i]=set()
            return True
        
        for i in range(n_cources):
            if dfs(i) == False:
                return False
        
        
        return True