class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<long, long>m;
        int res, len=nums.size();
        int thres=len/2;
        
        for(int i=0;i<len;i++){
            m[nums[i]]++;
            
            if(m[nums[i]]>thres)
                return nums[i];
        }
        
        return res;
    }
};