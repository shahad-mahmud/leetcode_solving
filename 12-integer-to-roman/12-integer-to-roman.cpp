class Solution {
public:
    string intToRoman(int num) {
        string res = "";
        
        num = build_res(res, num, 1000, "M");
        num = build_res(res, num, 900, "CM");
        num = build_res(res, num, 500, "D");
        num = build_res(res, num, 400, "CD");
        num = build_res(res, num, 100, "C");
        num = build_res(res, num, 90, "XC");
        num = build_res(res, num, 50, "L");
        num = build_res(res, num, 40, "XL");
        num = build_res(res, num, 10, "X");
        num = build_res(res, num, 9, "IX");
        num = build_res(res, num, 5, "V");
        num = build_res(res, num, 4, "IV");
        num = build_res(res, num, 1, "I");
        
        
        return res;
    }
    
    int build_res(string& res, int num, int divident, string sym){
        int temp = num / divident;
        for(int i = 0; i < temp; i++)
            res = res + sym;
        
        return num % divident;
    }
};