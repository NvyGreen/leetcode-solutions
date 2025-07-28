class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        int prev = cost[0];
        int curr = cost[1];

        for (int i = 2; i < n; ++i) {
            int res = cost[i] + min(prev, curr);
            prev = curr;
            curr = res;
        }

        return min(prev, curr);
    }
};
