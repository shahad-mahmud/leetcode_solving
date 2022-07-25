class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res=0, tmp=0, p1=0, p2=0, l=s.length();
        unordered_map<char,int>m;
        
        while(p2 < l){
            if(m[s[p2]] > 0 && m[s[p2]] > p1){
                p1=m[s[p2]];
                if(tmp > res) res=tmp;
                tmp=p2-p1+1;
            }
            else {
                
                tmp++;
                
            }
            m[s[p2]] = p2 + 1;
            p2++;
        }
        if(tmp > res) res=tmp;
        
        return res;
    }
};