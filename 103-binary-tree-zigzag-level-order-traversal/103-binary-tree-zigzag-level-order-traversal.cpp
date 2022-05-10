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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        vector<int> level_result;
        
        queue<pair<TreeNode*, int>> q;
        pair<TreeNode*, int> head;
        TreeNode* head_node;
        
        q.push(make_pair(root, 0));
        int prev_level = 0;
        
        while(!q.empty()){
            head = q.front();
            q.pop();
            
            head_node = head.first;
            if(head_node == nullptr) continue;
            
            q.push(make_pair(head_node->left, head.second + 1));
            q.push(make_pair(head_node->right, head.second + 1));
            
            if(head.second != prev_level){
                prev_level = head.second;
                if(prev_level&1)
                    result.push_back(level_result);
                else{
                    reverse(level_result.begin(), level_result.end());
                    result.push_back(level_result);
                }
                level_result.clear();
            }
            level_result.push_back(head_node->val);
        }
        prev_level += 1;
        if(!level_result.empty()){
            if(prev_level&1)
                result.push_back(level_result);
            else{
                reverse(level_result.begin(), level_result.end());
                result.push_back(level_result);
            }
        }
        
        return result;
    }
};