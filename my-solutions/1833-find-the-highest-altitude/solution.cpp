class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int curr_alt = 0;
        int max_alt = curr_alt;

        for (int i = 0; i < gain.size(); ++i) {
            curr_alt += gain[i];
            max_alt = max(max_alt, curr_alt);
        }

        return max_alt;
    }
};
