class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int checker[10], num;
        for(int i = 0; i < 10; i++) checker[i] = 0;
        
        // check rows
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                num = board[i][j];
                if(num >= '0' && num <= '9'){
                    num = num - '0';
                    checker[num]++;
                    if(checker[num] > 1) {
                        return false;
                    }
                }
            }
            for(int i = 0; i < 10; i++) checker[i] = 0;
        }
        
        // check columns
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                num = board[j][i];
                if(num >= '0' && num <= '9'){
                    num = num - '0';
                    checker[num]++;
                    if(checker[num] > 1) {
                        return false;
                    }
                }
            }
            for(int i = 0; i < 10; i++) checker[i] = 0;
        }
        
        // check matrix
        for(int i = 0; i < 9; i+=3){
            for(int j = 0; j < 9; j+=3){
                for(int k=i; k<i+3;k++){
                    for(int l=j; l<j+3; l++){
                        num = board[k][l];
                        if(num >= '0' && num <= '9'){
                            num = num - '0';
                            checker[num]++;
                            if(checker[num] > 1) {
                                return false;
                            }
                        }
                    }
                }
                for(int i = 0; i < 10; i++) checker[i] = 0;
            }
        }
        
        return true;
    }
};