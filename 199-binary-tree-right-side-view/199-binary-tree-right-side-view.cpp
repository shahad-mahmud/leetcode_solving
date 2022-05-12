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
    vector<int> rightSideView(TreeNode* root) {
        vector <int> result;
        queue<pair<TreeNode*, int>> q;
        pair<TreeNode*, int> head_pair;
        TreeNode* head;
        
        if(root != nullptr)
            q.push(make_pair(root, 0));
        int current_level = -1;
        
        while(!q.empty()){
            head_pair = q.front();
            head = head_pair.first;
            q.pop();
            
            if(head_pair.second != current_level){
                result.push_back(head->val);
                current_level += 1;
            }
            
            if(head->right != nullptr){
                q.push(make_pair(head->right, head_pair.second + 1));
            }
            if(head->left != nullptr){
                q.push(make_pair(head->left, head_pair.second + 1));
            }
        }
        
        return result;
    }
};