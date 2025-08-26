class Solution {
    static bool cmp (const vector<int>& x, const vector<int>& y) {
        return x[0] < y[0];
    }
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), cmp);

        vector<vector<int>> result;
        int a = intervals[0][0], b = intervals[0][1];

        for (int i = 1; i < intervals.size(); ++i) {
            int c = intervals[i][0], d = intervals[i][1];

            if (b >= c) {
                b = max(b, d);
            } else {
                result.push_back(vector<int>{a, b});
                a = c;
                b = d;
            }
        }

        result.push_back(vector<int>{a, b});
        return result;
    }
};
