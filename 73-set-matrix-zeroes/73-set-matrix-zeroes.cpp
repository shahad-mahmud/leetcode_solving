class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<int> is, js;
        int m = matrix.size();
        int n = matrix[0].size();
        
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(matrix[i][j] == 0){
                    is.push_back(i);
                    js.push_back(j);
                }
            }
        }
        
        int nis=is.size(), njs=js.size();
        for(int i=0; i<nis; i++){
            for(int j=0; j<n; j++){
                matrix[is[i]][j] = 0;
            }
        }
        
        for(int i=0; i<njs; i++){
            for(int j=0; j<m; j++){
                matrix[j][js[i]] = 0;
            }
        }
    }
};