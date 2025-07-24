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
    //My approach=>1
    // I will do Level order Traversal and after comptition of each level store that value in vector.

    vector<int> rightSideView(TreeNode* root) {
        vector<int>ans;
        if(root == nullptr)
            return ans;
        
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int levelsize = q.size();

            for (int i=0; i < levelsize; i++) {
                TreeNode* curr = q.front();
                q.pop();
                
                if (i == levelsize - 1)
                    ans.push_back(curr->val);
                
                if (curr->left)
                    q.push(curr->left);
                
                if (curr->right)
                    q.push(curr->right);
            }
        }

        return ans;
    }

};
