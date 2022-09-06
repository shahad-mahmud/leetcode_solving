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
    TreeNode* pruneTree(TreeNode* root) {
        bool p = to_prune(root);
        
        if(p==true)
            return nullptr;
        
        return root;
    }
    
    bool to_prune(TreeNode* root){
        bool prune=false;
        if(root->val==0) prune=true;
        
        if(root->left){
            bool temp=to_prune(root->left);
            if(temp){
                root->left=nullptr;
            }
            
            prune = prune && temp;
        }
        if(root->right){
            bool temp=to_prune(root->right);
            if(temp){
                root->right=nullptr;
            }
            
            prune = prune && temp;
        }
        
        return prune;
    }
};