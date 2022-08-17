class Solution {
public:
    static bool comp(pair<int, int>&a, pair<int, int>&b){
        return a.second>b.second;
    }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        
        unordered_map<int, int> m;
        int len = nums.size();
        
        for(int i=0; i<len; i++){
            m[nums[i]]++;
        }
        
        vector<pair<int, int>> v = {m.begin(), m.end()};        
        sort(v.begin(), v.end(), comp);
        
        for(int i=0; i<k; i++){
            res.push_back(v[i].first);
        }
        
        return res;
    }
    
};