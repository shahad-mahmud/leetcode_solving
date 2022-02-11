class Solution {
public:
    int maxPower(string s) {
        int max=0, c=0;
        char prev = '#';
        for(int i=0; i<s.length(); i++){
            if(s[i] == prev)
                c++;
            else{
                prev = s[i];
                if(c>max)
                    max = c;
                c = 1;
            }
        }
        if(c>max){
            max=c;
        }
        return max;
    }
};