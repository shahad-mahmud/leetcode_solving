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
    
    bool isPossible(vector<int>& nums, int pos, int size, int *mem){
        if(pos == size - 1) return true;
        if(pos >= size) return false;
        if(pos != size -1 && nums[pos] == 0) return false;
        
        if(mem[pos] != -1) return mem[pos];
        
        vector<bool> temp_res;
        for(int i=1; i<=nums[pos]; i++){
            mem[pos] = isPossible(nums, pos + i, size, mem);
            temp_res.push_back(mem[pos]);
        }
        
        for(auto i=temp_res.begin(); i != temp_res.end(); i++)
            if(*i == true)
                return true;
        
        return false;
    }
};