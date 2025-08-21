class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int dup = 0;
        int curr = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == curr) {
                if (dup == 1) {
                    nums.erase(nums.begin() + i);
                    --i;
                } else {dup = 1;}
            } else {
                dup = 0;
                curr = nums[i];
            }
        }

        return nums.size();
    }
};
