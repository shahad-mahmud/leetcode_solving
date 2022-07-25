class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res=0, tmp=0, p1=0, p2=0, l=s.length();
        // auto m = reset_map();
        unordered_map<char,int>m;
        
        while(p2 < l){
            m[s[p2]]++;
            
            if(m[s[p2]] > 1){
                p1++;
                p2=p1;
                m.clear();
                if(tmp > res) res=tmp;
                tmp=0;
            }
            else {
                tmp++;
                p2++;
            }
        }
        if(tmp > res) res=tmp;
        
        return res;
    }
    
    unordered_map<char, int> reset_map(){
        unordered_map<char, int> m;
        
        for(int i=0; i<128; i++){
            m[char(i)] = 0;
        }
        
        return m;
    }
};