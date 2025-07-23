class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int low = 0;
        int high = nums.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            bool leftSmall = ((mid - 1) < 0 || nums[mid] > nums[mid - 1]);
            bool rightSmall = ((mid + 1) >= nums.size() || nums[mid] > nums[mid + 1]);

            if (leftSmall && rightSmall) {
                return mid;
            } else if (leftSmall) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return -1;
    }
};
