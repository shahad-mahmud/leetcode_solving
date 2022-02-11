class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        vector<int> result;
        if(tomatoSlices & 1)
            return result;
        if(tomatoSlices < 2 * cheeseSlices)
            return result; 
        if(tomatoSlices > 4 * cheeseSlices)
            return result;
        
        result.push_back((tomatoSlices-2*cheeseSlices)/2);
        result.push_back(cheeseSlices-result[0]);
        return result;
    }
};