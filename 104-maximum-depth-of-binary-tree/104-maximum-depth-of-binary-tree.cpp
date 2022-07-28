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
    int maxDepth(TreeNode* root) {
        if(root==nullptr) return 0;
        
        queue<pair<TreeNode*, int>>q;
        pair<TreeNode*, int>head;
        int depth=-1;
        
        q.push(make_pair(root, 0));
        while(!q.empty()){
            head=q.front();
            q.pop();
            
            if(head.second > depth) depth=head.second;

            if(head.first->left!=nullptr) q.push(make_pair(head.first->left, head.second+1));
            if(head.first->right!=nullptr) q.push(make_pair(head.first->right, head.second+1));
        }
        
        return depth+1;
    }
};