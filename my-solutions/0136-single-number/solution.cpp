class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int index = 0;

        for (int num : nums) {
            index = index ^ num;
        }

        return index;
    }
};
