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
    TreeNode* searchBST(TreeNode* root, int val) {
        if (root == nullptr) {
            return nullptr;
        } else if (root->val == val) {
            return root;
        } else {
            TreeNode* testLeft = searchBST(root->left, val);
            if (testLeft != nullptr) {
                return testLeft;
            } else {
                return searchBST(root->right, val);
            }
        }
    }
};
