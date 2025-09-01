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
    TreeNode* helper(deque<int> &preOrderQueue, vector<int> inOrder) {
        if (!inOrder.empty()) {
            int val = preOrderQueue.front();
            preOrderQueue.pop_front();

            auto index = find(inOrder.begin(), inOrder.end(), val);
            int idx = index - inOrder.begin();

            vector<int> leftInOrder(inOrder.begin(), inOrder.begin() + idx);
            vector<int> rightInOrder(inOrder.begin() + idx + 1, inOrder.end());

            TreeNode* root = new TreeNode(val);
            root->left = helper(preOrderQueue, leftInOrder);
            root->right = helper(preOrderQueue, rightInOrder);
            return root;
        }
        return nullptr;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        deque<int> preOrderQueue(preorder.begin(), preorder.end());
        return helper(preOrderQueue, inorder);
    }
};
