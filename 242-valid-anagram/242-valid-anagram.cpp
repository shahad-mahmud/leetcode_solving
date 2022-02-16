class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) return false;
        
        int size=s.length();
        vector<int> s_counter(26, 0), t_counter(26, 0);
        
        for(int i = 0; i < size; i++){
            s_counter[s[i] - 'a']++;
            t_counter[t[i] - 'a']++;
        }
        
        for(int i = 0; i < 26; i++){
            if(s_counter[i] != t_counter[i])
                return false;
        }
        
        return true;
    }
};