class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int, int> fm, hm;
        
        int len=nums.size();
        
        for(int i=0;i<len;i++){
            fm[nums[i]]++;
        }
        
        for(int num: nums){
            if(fm[num]==0) continue;
            
            if(hm[num]>0){
                fm[num]--;
                hm[num]--;
                
                hm[num+1]++;
            }
            else if(fm[num]>0 && fm[num+1]>0 && fm[num+2]>0){
                fm[num]--;
                fm[num+1]--;
                fm[num+2]--;
                
                hm[num+3]++;
            }
            else return false;
        }
        
        return true;
    }
};