class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        unordered_map<long long, int> map;
        vector <int> res;
        auto original = arr;
        
        sort(arr.begin(), arr.end());
        int rank = 1;
        
        for(auto i=arr.begin(); i!=arr.end(); i++){
            if(map.find(*i) == map.end()){
            map[*i] = rank;
            rank++;}
        }
        
        for(auto i=original.begin(); i!=original.end(); i++){
            res.push_back(map[*i]);
        }
        
        return res;
    }
};