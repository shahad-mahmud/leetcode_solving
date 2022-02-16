class Solution {
public:
    bool canJump(vector<int>& nums) {
        int size = nums.size();
        vector<bool> is_possible(size, false);
        
        is_possible[size-1] = true;
        
        for(int i = size -2; i >= 0; i--){
            for(int j = 1; j <= nums[i]; j++){
                if(i+j >= size) break;
                if(is_possible[i+j]){
                    is_possible[i] = true; 
                    break;
                }
            }
        }
        
        return is_possible[0];
    }
};