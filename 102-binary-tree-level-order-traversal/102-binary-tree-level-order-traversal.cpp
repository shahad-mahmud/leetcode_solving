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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        vector<int> level;
        queue<pair<TreeNode*, int>> q;
        pair<TreeNode*, int> head_pair;
        
        q.push(make_pair(root, 0));
        int prev_level = 0;
        
        while(!q.empty()){
            head_pair = q.front();
            TreeNode* head = head_pair.first;
            q.pop();
            
            if(head == nullptr) continue;
            
            q.push(make_pair(head -> left, head_pair.second + 1));
            q.push(make_pair(head -> right, head_pair.second + 1));
            
            if(head_pair.second != prev_level){
                prev_level = head_pair.second;
                result.push_back(level);
                level.clear();
            }
            level.push_back(head -> val);
        }
        
        if(!level.empty())
            result.push_back(level);
        return result;
    }
};