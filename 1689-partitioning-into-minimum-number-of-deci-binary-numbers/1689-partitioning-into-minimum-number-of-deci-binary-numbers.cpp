class Solution {
public:
    int minPartitions(string n) {
        int res=0;
        int len=n.length();
        
        for(int i=0;i<len;i++){
            if(n[i] - '0' > res) res=n[i] - '0';
        }
        
        
        return res;
    }
};