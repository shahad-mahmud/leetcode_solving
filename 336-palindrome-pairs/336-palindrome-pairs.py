class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        rev, res={}, []
        
        for i, w in enumerate(words):
            rev[w[::-1]]=i
        
        for i, w in enumerate(words):
            if w in rev and rev[w]!=i:
                res.append([i, rev[w]])
            
            if w!="" and "" in rev and w==w[::-1]:
                res.append([i, rev[""]])
                res.append([rev[""], i])
            
            for j in range(len(w)):
                if w[j:] in rev and w[:j]==w[j-1::-1]:
                    res.append([rev[w[j:]], i])
                if w[:j] in rev and w[j:]==w[:j-1:-1]:
                    res.append([i, rev[w[:j]]])
        
        return res
        