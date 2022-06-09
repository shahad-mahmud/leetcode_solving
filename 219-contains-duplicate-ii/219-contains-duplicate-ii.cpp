class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<long, int> m;
        
        int len = nums.size();
        
        for(int i = 0; i < len; i++){
            if(m[nums[i]]>0){
                if(i + 1 - m[nums[i]] <= k) return true;
            }
            m[nums[i]] = i + 1;
        }
        
        return false;
    }
};