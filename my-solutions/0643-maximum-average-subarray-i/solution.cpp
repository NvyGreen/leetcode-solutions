class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int max_sum = 0;
        int current_sum = 0;
        
        for (int i = 0; i < k; ++i) {
            current_sum += nums[i];
        }
        max_sum = current_sum;
        
        for (int i = k; i < nums.size(); ++i) {
            current_sum += nums[i];
            current_sum -= nums[i - k];
            max_sum = max(current_sum, max_sum);
        }
        
        return max_sum / double(k);
    }
};
