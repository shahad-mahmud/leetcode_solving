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
    bool isvalid=true;
    long long prev=-LLONG_MAX;
    
    bool isValidBST(TreeNode* root) {
        inorder_test(root);
        
        return isvalid;
    }
    
    void inorder_test(TreeNode* root){
        if(root != nullptr){
            inorder_test(root->left);
            if(prev >= root->val){
                isvalid=false;
                return;
            }
            prev=root->val;
            inorder_test(root->right);
        }   
    }
};