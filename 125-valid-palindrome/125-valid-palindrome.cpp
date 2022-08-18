class Solution {
public:
    bool isPalindrome(string s) {
        string clean="";
        int len = s.length();
        
        for(int i=0; i<len;i++){
            if(s[i] >= 'A' && s[i] <= 'Z'){
                clean+= s[i] + 32;
            }
            else if((s[i] >= '0' && s[i] <= '9') || (s[i] >= 'a' && s[i] <= 'z')){
                clean+=s[i];
            }
        }
        cout<<clean<<endl;
        string temp=clean;
        reverse(clean.begin(), clean.end());
        return temp==clean;
    }
};