class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build the graph
        tickets.sort()
        graph = defaultdict(lambda: [])
        for s, d in tickets:
            graph[s].append(d)
        
        res = ['JFK']
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if not graph[node]:
                return False
            
            childs = list(graph[node])
            for i in range(len(childs)):
                graph[node].pop(i)
                res.append(childs[i])
                
                if dfs(childs[i]):
                    return True
                
                graph[node].insert(i, childs[i])
                res.pop()
            return False
        
        dfs('JFK')
        return res
            
        