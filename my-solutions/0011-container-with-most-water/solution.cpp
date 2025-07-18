class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;

        while (left < right) {
            int min_line = min(height[left], height[right]);
            int current_area = min_line * (right - left);
            max_area = max(current_area, max_area);

            if (min_line == height[left]) {
                ++left;
            } else {
                --right;
            }
        }

        return max_area;
    }
};
