class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<long, int> m;
        
        int len = nums.size();
        for(int i = 0; i < len; i++) m[nums[i]]++;
        if (len > m.size()) return true;
        return false;
    }
};