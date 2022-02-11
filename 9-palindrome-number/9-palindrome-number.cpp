class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        
        long long new_num = 0;
        int org = x;
        while(x){
            new_num = new_num * 10 + x % 10;
            x /= 10;
        }
        
        if(new_num == org)
            return true;
        return false;
    }
};