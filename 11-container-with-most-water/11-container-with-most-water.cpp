class Solution {
public:
    int min(int a, int b){
        if (a<b) return a;
        return b;
    }
    int maxArea(vector<int>& height) {
        int len = height.size();
        long long res = -1, area;
        int p1 = 0, p2 = len - 1;
        
        while(p1 < len && p2 >= 0){
            area = min(height[p1], height[p2]) * (p2 - p1);
            if(area > res) res = area;
            
            if (height[p1] <= height[p2]){
                p1++;
            }
            else p2--;
        }
        
        return res;
    }
};