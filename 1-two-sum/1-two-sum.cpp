class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        unordered_map<int, int> map;
        int len = nums.size();
        
        for(int i = 0; i < len; i++){
            if(map.find(target-nums[i]) != map.end()){
                res.push_back(map[target-nums[i]]);
                res.push_back(i);
                
                return res;
            }
            map[nums[i]] = i;
        }
        
        return res;
    }
};