class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        vector<vector<string>> result;
        
        int size = strs.size();
        
        for(int i = 0; i< size; i++){
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            
            map[temp].push_back(strs[i]);
        }
        
        for(auto item=map.begin(); item!=map.end(); item++)
            result.push_back(item->second);
          
        return result;
    }
};