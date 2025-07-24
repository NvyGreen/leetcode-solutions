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
    int goodNodes(TreeNode* root, int maxVal=INT_MIN) {
        if (root == nullptr) {
            return 0;
        }

        maxVal = max(maxVal, root->val);
        int left = goodNodes(root->left, maxVal);
        int right = goodNodes(root->right, maxVal);

        if (root->val >= maxVal) {
            return left + right + 1;
        }
        return left + right;
    }
};
