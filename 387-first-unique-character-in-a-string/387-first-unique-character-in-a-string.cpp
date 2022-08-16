class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> m;
        int len = s.length();
        
        for(int i=0; i<len; i++){
            m[s[i]]++;
        }
        
        for(int i=0; i<len; i++){
            if(m[s[i]]==1) return i;
        }
        
        return -1;
    }
};