class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int pairs = 0;
        map<vector<int>, int> columns;

        for (int i = 0; i < grid[0].size(); ++i) {
            vector<int> col;

            for (int j = 0; j < grid.size(); ++j) {
                col.push_back(grid[j][i]);
            }

            if (columns.find(col) == columns.end()) {
                columns[col] = 1;
            } else {
                ++columns[col];
            }
        }

        for (const vector<int>& row : grid) {
            if (columns.find(row) != columns.end()) {
                pairs += columns[row];
            }
        }

        return pairs;
    }
};
