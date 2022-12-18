class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c:[] for c in range(numCourses)}
        for cond in prerequisites:
            graph[cond[0]].append(cond[1])
        
        visited, cur_path = set(), set()
        outputs = []
        def dfs(c):
            if c in cur_path:
                # cycle
                return False
            if c in visited:
                # already added to ouputs
                return True
            
            cur_path.add(c)
            for child in graph[c]:
                if not dfs(child):
                    return False
            cur_path.remove(c)
            
            # add to outputs
            outputs.append(c)
            visited.add(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return outputs
        