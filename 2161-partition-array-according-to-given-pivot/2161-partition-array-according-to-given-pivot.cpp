class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> smalls, bigs;
        int pivot_count=0, len=nums.size();
        
        for(int i=0;i<len;i++){
            if(nums[i] == pivot) pivot_count++;
            else if(nums[i] < pivot) smalls.push_back(nums[i]);
            else bigs.push_back(nums[i]);
        }
        
        int big_count=bigs.size();
        for(int i=0;i<pivot_count;i++) smalls.push_back(pivot);
        for(int i=0;i<big_count;i++) smalls.push_back(bigs[i]);
        
        return smalls;
    }
};