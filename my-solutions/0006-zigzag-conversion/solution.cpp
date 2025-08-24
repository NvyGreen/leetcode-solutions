class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows==1) return s;
        string res = "";
        int n = s.size();

        int increment = 2 * (numRows-1);

        for(int r=0;r<numRows;r++){
            for(int i=r; i<n;i+=increment){
                res += s[i];

                if(r>0 && r<numRows-1 && i + increment - 2 * r < n){
                    res += s[i + increment - 2 * r];
                }
            }
        }
        return res;
    }
};
