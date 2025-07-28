class Solution {
public:
    void finder(int start, int k, int sum, vector<int>& path, vector<vector<int>> &result) {
        if (path.size() == k && sum == 0) {
            result.push_back(path);
            return;
        }

        if (path.size() > k || sum < 0) {
            return;
        }

        for (int i = start; i <= 9; ++i) {
            path.push_back(i);
            finder(i + 1, k, sum - i, path, result);
            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> result;
        vector<int> path;
        finder(1, k, n, path, result);
        return result;
    }
};
