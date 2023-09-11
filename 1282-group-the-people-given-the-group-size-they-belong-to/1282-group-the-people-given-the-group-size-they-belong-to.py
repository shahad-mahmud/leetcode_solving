class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        
        for i, g in enumerate(groupSizes):
            if len(groups[g]) == 0 or len(groups[g][-1]) == g:
                groups[g].append([])
            
            groups[g][-1].append(i)
        
        return [v for g in groups.values() for v in g]
        