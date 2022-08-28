class Solution {
public:
    int compareVersion(string v1, string v2) {
        int i=0,j=0;
        bool leading1=true, leading2=true;
        int l1=v1.length(), l2=v2.length();
        char c1=v1[0], c2=v2[0];
        
        long long temp1=0, temp2=0;
        
        while(i<l1 || j<l2){
            temp1=temp2=0;
            
            while(i<l1 && v1[i]!='.'){
                temp1 += temp1 * 10 + (v1[i]-'0');
                i++;
            }
            
            while(j<l2 && v2[j]!='.'){
                temp2 += temp2 * 10 + (v2[j]-'0');
                j++;
            }
            
            if(temp1>temp2) return 1;
            if(temp1<temp2) return -1;
            
            i++, j++;
        }
        
        return 0;        
    }
};