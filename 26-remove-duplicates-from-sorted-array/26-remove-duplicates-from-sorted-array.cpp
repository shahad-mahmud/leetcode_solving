class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_map<int,int> m;
        int len=nums.size(), last_unique_index=0;
        
        for(int i=0;i<len;i++){
            m[nums[i]]++;
            
            if(m[nums[i]]==1){
                nums[last_unique_index]=nums[i];
                last_unique_index++;
            }
        }
        
        return last_unique_index;
    }
};