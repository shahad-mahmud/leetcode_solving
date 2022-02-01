class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indices;
        for(auto i = nums.begin(); i != nums.end(); i++){
            int to_find = target - *i;
            for(auto j = nums.begin(); j != nums.end(); j++){
                if(i != j and to_find == *j){
                    indices.push_back(i - nums.begin());
                    indices.push_back(j - nums.begin());
                    
                    return indices;
                }
            }
        }
        
        return indices;
    }
};