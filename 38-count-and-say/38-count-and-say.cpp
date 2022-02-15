class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) return "1";
        
        string prev_say = countAndSay(n-1);
        int count = 1;
        int len = prev_say.length();
        char prev_digit = prev_say[0];
        string result;
        
        for(int i = 1; i < len; i++){
            if(prev_say[i] == prev_digit) count++; 
            else{
                result += to_string(count) + prev_digit;
                count = 1;
                prev_digit = prev_say[i];
            }
        }
        
        if(count > 0){
            result += to_string(count) + prev_digit;
        }
        
        return result;
    }
};