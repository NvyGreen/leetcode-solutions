class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> num_ones(n+1, 0);

        for (int i = 0; i < num_ones.size(); ++i) {
            int n = i;
            while (n > 0) {
                num_ones[i] += (n & 1);
                n >>= 1;
            }
        }

        return num_ones;
    }
};
