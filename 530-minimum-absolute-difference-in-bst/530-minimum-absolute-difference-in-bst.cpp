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
    int getMinimumDifference(TreeNode* root) {
        queue<TreeNode*> q;
        TreeNode* head;
        vector<int> vals;
        
        q.push(root);
        
        while(!q.empty()){
            head = q.front();
            q.pop();
            
            if(head==nullptr) continue;
            
            vals.push_back(head->val);
            q.push(head->left);
            q.push(head->right);
        }
        
        sort(vals.begin(), vals.end());
        
        int min=100005, temp;
        int len = vals.size();
        for(int i=0; i < len-1; i++){
            temp = abs(vals[i]-vals[i+1]);
            if(temp < min) min=temp;
        }
        
        return min;
    }
};