class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector <string> result;
        if(digits.length() == 0) return result;
        
        unordered_map<char, string> digit_to_chars;
        
        digit_to_chars['2'] = "abc";
        digit_to_chars['3'] = "def";
        digit_to_chars['4'] = "ghi";
        digit_to_chars['5'] = "jkl";
        digit_to_chars['6'] = "mno";
        digit_to_chars['7'] = "pqrs";
        digit_to_chars['8'] = "tuv";
        digit_to_chars['9'] = "wxyz";
        
        string chars = digit_to_chars[digits[0]];
        int len = chars.length();

        for(int i=0; i < len; i++){
            string s;
            s += chars[i];
            cout << s;
            result.push_back(s);
        }
        
        for(int i=1; i<digits.length(); i++){
            chars = digit_to_chars[digits[i]];
            result = cartesian_product(result, chars);
        }
        
        
        return result;
    }
    
    vector<string> cartesian_product(vector<string> set_a, string set_b){
        vector<string> result;
        
        for(auto i=0; i < set_a.size(); i++){
            for(auto j=0; j < set_b.length(); j++){
                string s;
                s += set_a[i];
                s += set_b[j];
                result.push_back(s);
            }
        }
        
        return result;
    }
};