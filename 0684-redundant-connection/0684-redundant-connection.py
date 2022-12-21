class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        pars = [i for i in range(n+1)]
        ranks = [1]*(n+1)
        
        def find(n):
            p=pars[n]
            while p!=pars[p]:
                pars[p]=pars[pars[p]]
                p=pars[p]
            return p
        
        for a,b in edges:
            pa,pb = find(a), find(b)
            
            if pa==pb:
                return [a,b]
            elif ranks[pa]>=ranks[pb]:
                ranks[pa]+=ranks[pb]
                pars[pb]=pa
            else:
                ranks[pb]+=ranks[pa]
                pars[pa]=pb