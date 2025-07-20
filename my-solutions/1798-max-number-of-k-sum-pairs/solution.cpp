class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int sums = 0;
        sort(nums.begin(), nums.end());
        
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            if ((nums[left] + nums[right]) == k) {
                ++sums;
                ++left;
                --right;
            } else if ((nums[left] + nums[right]) < k) {
                ++left;
            } else {
                --right;
            }
        }

        return sums;
    }
};
