class Solution {
    int m, n;
    bool dfs(int idx, int r, int c, vector<vector<char>>& board, string &word)
    {
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != word[idx]) return 0;
        if (idx == word.size() - 1) return 1;

        static const int dir[4][2] = {{1, 0}, {0, 1}, {0, -1}, {-1, 0}};

        char temp = board[r][c];
        board[r][c] = '#';
        bool found = 0;

        for (int i = 0; i < 4; ++i)
        {
            int nr = r + dir[i][0];
            int nc = c + dir[i][1];
            if (dfs(idx + 1, nr, nc, board, word))
            {
                board[r][c] = temp;
                return 1;
            }
        }

        board[r][c] = temp;
        return 0;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if(board[i][j] == word[0] && dfs(0, i, j, board, word)) return 1;
            }
        }
        return 0;
    }
};
