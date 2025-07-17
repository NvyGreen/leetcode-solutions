class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            int left_sum = accumulate(nums.begin(), nums.begin() + i, 0);
            int right_sum = accumulate(nums.begin() + i + 1, nums.end(), 0);

            if (left_sum == right_sum) {
                return i;
            }
        }

        return -1;
    }
};
