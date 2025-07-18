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
    vector<int> get_leaves(TreeNode* root) {
        vector<int> leaves;

        if (root == nullptr) {
            return leaves;
        } else if (root->left == nullptr && root->right == nullptr) {
            leaves.push_back(root->val);
            return leaves;
        } else {
            vector<int> left_leaves = get_leaves(root->left);
            vector<int> right_leaves = get_leaves(root->right);

            copy(left_leaves.begin(), left_leaves.end(), back_inserter(leaves));
            copy(right_leaves.begin(), right_leaves.end(), back_inserter(leaves));
            return leaves;
        }
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaves1 = get_leaves(root1);
        vector<int> leaves2 = get_leaves(root2);

        return leaves1 == leaves2;
    }
};
