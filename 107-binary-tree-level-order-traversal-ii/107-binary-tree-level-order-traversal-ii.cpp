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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        
        if(root == nullptr) return res;
        
        vector<int> temp;
        queue<pair<TreeNode*, int>> q;
        pair<TreeNode*, int> head;
        
        q.push(make_pair(root, 0));
        int prev_level = 0;
        
        while(!q.empty()){
            head = q.front();
            q.pop();
            
            if(head.second != prev_level){
                res.push_back(temp);
                temp.clear();
                prev_level=head.second; 
            }
            
            temp.push_back(head.first->val);
            
            if(head.first->left != nullptr) q.push(make_pair(head.first->left, head.second + 1));
            if(head.first->right != nullptr) q.push(make_pair(head.first->right, head.second + 1));
        }
        
        if(!temp.empty()){
            res.push_back(temp);
        }
        
        reverse(res.begin(), res.end());
        return res;
    }
};