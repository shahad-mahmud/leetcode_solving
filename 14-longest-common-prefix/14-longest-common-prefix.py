class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for i in range(len(strs[0])):
            res=strs[0][:i+1]   
            
            if not all(w.startswith(res) for w in strs):
                return res[:-1]
            
        return res