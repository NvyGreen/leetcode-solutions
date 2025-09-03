class Solution {
private:
    void dfs(int row, int col, vector<vector<int>>& vis,
             vector<vector<char>>& board) {
        int n = board.size(), m = board[0].size();
        vis[row][col] = 1;
        int delrow[] = {-1, 0, 1, 0};
        int delcol[] = {0, 1, 0, -1};

        for (int i = 0; i < 4; i++) {
            int nrow = row + delrow[i];
            int ncol = col + delcol[i];
            if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m &&
                !vis[nrow][ncol] && board[nrow][ncol] == 'O') {
                dfs(nrow, ncol, vis, board);
            }
        }
    }

public:
    void solve(vector<vector<char>>& board) {
        int n = board.size(), m = board[0].size();
        vector<vector<int>> vis(n, vector<int>(m, 0));

        // traverse boundary rows
        for (int i = 0; i < m; i++) {
            // 1st row
            if (!vis[0][i] && board[0][i] == 'O') {
                dfs(0, i, vis, board);
            }

            // last row
            if (!vis[n - 1][i] && board[n - 1][i] == 'O') {
                dfs(n - 1, i, vis, board);
            }
        }

        // traverse boundary cols
        for (int i = 0; i < n; i++) {
            // 1st row
            if (!vis[i][0] && board[i][0] == 'O') {
                dfs(i, 0, vis, board);
            }

            // last row
            if (!vis[i][m - 1] && board[i][m - 1] == 'O') {
                dfs(i, m - 1, vis, board);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!vis[i][j] && board[i][j] == 'O')
                    board[i][j] = 'X';
            }
        }
    }
};
