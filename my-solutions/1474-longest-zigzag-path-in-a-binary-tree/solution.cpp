/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans = 0;

    void solve(TreeNode* root, int steps, bool goLeft) {
        if (!root) {
            return;
        }

        ans = max(ans, steps);

        if (goLeft) {
            solve(root->right, steps + 1, false);
            solve(root->left, 1, true);
        } else {
            solve(root->left, steps + 1, true);
            solve(root->right, 1, false);
        }
    }

    int longestZigZag(TreeNode* root) {
        solve(root, 0, true);
        solve(root, 0, false);
        
        return ans;
    }
};
