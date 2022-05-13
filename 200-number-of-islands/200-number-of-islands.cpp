class Solution {
public:
    bool flags[301][301];
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int columns = grid[0].size();
        int count = 0;
        
        for(int i=0;i<rows;i++){
            for(int j=0;j<columns;j++){
                if(grid[i][j] == '1' && (flags[i][j] == false))
                    count += visit_island(i, j, grid, rows, columns);
            }
        }
        
        return count;
    }
    
    int visit_island(int i, int j, vector<vector<char>>& grid, int rows, int columns){
        pair<int,int> front;
        queue<pair<int,int>>q;
        q.push(make_pair(i,j));
        while(!q.empty()){
            front = q.front();
            q.pop();
            
            i = front.first;
            j = front.second;
            
            if(i <0 || j <0 || i >= rows || j >= columns || flags[i][j]) continue;
            if(grid[i][j] == '0') continue;
            
            flags[i][j] = true;
            
            q.push(make_pair(i-1, j));
            q.push(make_pair(i+1, j));
            q.push(make_pair(i, j-1));
            q.push(make_pair(i, j+1));
        }
        return 1;
    }
};