class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m = maze.size(), n = maze[0].size(), d = 0;
        queue<pair<int, int>> q;
        q.push({entrance[0], entrance[1]});
        maze[entrance[0]][entrance[1]] = '+';
        const int dirs[5] = {0, 1, 0, -1, 0};
        while (!q.empty()) {
            for (int f = 0, len = q.size(); f < len; ++f) {
                auto [i, j] = q.front(); q.pop();
                for (int k = 0; k < 4; ++k) {
                    int x = i + dirs[k], y = j + dirs[k + 1];
                    if (x < 0 || y < 0 || x == m || y == n || maze[x][y] != '.') continue;
                    if (x == 0 || y == 0 || x == m - 1 || y == n - 1) return d + 1;
                    maze[x][y] = '+';
                    q.push({x, y});
                }
            }
            ++d;
        }
        return -1;
    }
};
