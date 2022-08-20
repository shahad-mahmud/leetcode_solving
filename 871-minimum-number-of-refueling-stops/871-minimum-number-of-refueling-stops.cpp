class Solution {
public:
    int minRefuelStops(int target, int fuel, vector<vector<int>>& stations){
        priority_queue<int> pq;

        vector<int> temp={target, -INT_MAX};
        stations.push_back(temp);
        
        int count=0, prev_distance=0;
        
        for(vector<int> station:stations){
            fuel -= (station[0] - prev_distance);
            
            while(!pq.empty() && fuel<0){
                fuel += pq.top();
                pq.pop();
                
                count++;
            }
            
            if(fuel<0) return -1;
            pq.push(station[1]);
            prev_distance=station[0];
        }
        
        return count;
    }
        
};