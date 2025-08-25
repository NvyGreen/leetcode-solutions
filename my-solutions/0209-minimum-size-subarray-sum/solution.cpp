class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, r = 0;
        int n = nums.size();
        long sum = 0;
        int minLength = INT_MAX;

        while (r < n) {
            sum += nums[r];
            while (sum >= target) {
                minLength = min(minLength, (r - l + 1));
                if (minLength == 1) {return 1;}
                sum -= nums[l];
                l++;
            }
            r++;
        }

        return (minLength == INT_MAX) ? 0 : minLength;
    }
};
