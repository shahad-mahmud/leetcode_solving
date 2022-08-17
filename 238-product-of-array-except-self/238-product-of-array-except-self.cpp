class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        int len=nums.size();
        
        int prefix[len], suffix[len];
        int j=len-2, i=1;
        
        prefix[0]=suffix[j+1]=1;
        
        while(i<len){
            prefix[i]=prefix[i-1]*nums[i-1];
            suffix[j]=suffix[j+1]*nums[j+1];
            
            i++;
            j--;
        }
        
        for(i=0;i<len;i++)
            res.push_back(prefix[i]*suffix[i]);
        
        return res;
    }
};