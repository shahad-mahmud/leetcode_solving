class Solution {
public:
    bool isValid(string s) {
        map<char, char> m;
        m[')'] = '(';
        m['}'] = '{';
        m[']'] = '[';
        
        int len=s.length();
        stack<char> checker;
        
        for(int i=0; i<len; i++){
            if (s[i] == '(' || s[i] == '{' || s[i] == '['){
                checker.push(s[i]);
            }
            else if(!checker.empty()){
                if(checker.top() == m[s[i]])
                    checker.pop();
                else return false;
            }
            else return false;
        }
        if(!checker.empty()) return false;
        
        return true;
    }
};