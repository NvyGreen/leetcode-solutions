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
    int count = 0;

    int pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        helperPathSum(root, targetSum, path);
        return count;
    }

    void helperPathSum(TreeNode* root, int targetSum, vector<int>& path) {
        if (root == nullptr) {
            return;
        }

        path.push_back(root->val);
        long long sum = 0;

        for (long long i = path.size() - 1; i >= 0; --i) {
            sum += path[i];
            if (sum == targetSum) {
                ++count;
            }
        }

        helperPathSum(root->left, targetSum, path);
        helperPathSum(root->right, targetSum, path);

        path.pop_back();
    }
};
