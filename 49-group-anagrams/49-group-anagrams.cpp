class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>>m;
        int len=strs.size();
        string t;
        
        for(int i=0;i<len;i++){
            t = strs[i];
            sort(t.begin(), t.end());
            m[t].push_back(strs[i]);
        }
        
        vector<vector<string>> res;
        for(auto i:m){
            res.push_back(i.second);
        }
        
        return res;
    }
};