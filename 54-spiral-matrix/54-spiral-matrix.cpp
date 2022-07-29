class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int rows=matrix.size();
        int cols=matrix[0].size();
        
        int top, bottom, left, right, op_mode;
        top=0, left=0;
        bottom=rows-1, right=cols-1;
        
        op_mode=1;
        vector<int> res;
        
        while(top<=bottom && left<=right){
            if(op_mode==1){
                for(int i=left;i<=right;i++)
                    res.push_back(matrix[top][i]);
                
                op_mode=2;
                top++;
            }
            else if(op_mode==2){
                for(int j=top;j<=bottom;j++)
                    res.push_back(matrix[j][right]);
                
                op_mode=3;
                right--;
            }
            else if(op_mode==3){
                for(int i=right;i>=left;i--)
                    res.push_back(matrix[bottom][i]);
                
                op_mode=4;
                bottom--;
            }
            else if(op_mode==4){
                for(int j=bottom;j>=top;j--)
                    res.push_back(matrix[j][left]);
                
                op_mode=1;
                left++;
            }
        }
        
        return res;
    }
};