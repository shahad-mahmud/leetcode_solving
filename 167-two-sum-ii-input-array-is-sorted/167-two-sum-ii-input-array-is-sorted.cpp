class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int len = numbers.size();
        unordered_map<int, int> map;
        
        for(int i=0; i<len; i++){
            if(map.find(target - numbers[i]) != map.end()){
                res.push_back(1 + map[target - numbers[i]]);
                res.push_back(i + 1);
                
                return res;
            }
            map[numbers[i]] = i;
        }
        
        return res;
    }
};