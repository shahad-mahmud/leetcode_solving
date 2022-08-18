class Solution {
public:
    static bool comp(pair<int,int>a, pair<int,int>b){
        return a.second > b.second;
    }
    
    int minSetSize(vector<int>& arr) {
        int len=arr.size(), res=0;
        int target=len/2;
        unordered_map<int, int>m;
        
        for(int i=0;i<len;i++){
            m[arr[i]]++;
        }
        
        vector<pair<int,int>> v={m.begin(), m.end()};
        sort(v.begin(), v.end(), comp);
        int v_len=v.size();
        
        for(int i=0;i<v_len;i++){
            len -= v[i].second;
            res++;
            
            if(len <= target) return res;
        }
        
        return res;
    }
};