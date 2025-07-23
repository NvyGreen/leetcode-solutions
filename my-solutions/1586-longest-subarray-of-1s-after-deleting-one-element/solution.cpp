class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0;
        int right = 0;
        bool elementDeleted = false;
        int nextLeftPosition = 0;
        int maxOnes = 0;

        while (left <= right && right < nums.size()) {
            if (nums[right] == 1) {
                ++right;
            } else {
                if (!elementDeleted) {
                    elementDeleted = true;
                    nextLeftPosition = ++right;
                } else {
                    maxOnes = max(maxOnes, right - 1 - left);
                    left = nextLeftPosition;
                    nextLeftPosition = ++right;
                }
            }
        }

        maxOnes = max(maxOnes, right - 1 - left);

        return maxOnes;
    }
};
