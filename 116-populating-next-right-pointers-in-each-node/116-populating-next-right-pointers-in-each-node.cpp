/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        Node* head_node;
        
        queue<pair<Node*, int>> q;
        pair<Node*, int> head;
        q.push(make_pair(root, 0));
        int level = 0;
        
        while(!q.empty()){
            head = q.front();
            head_node = head.first;
            q.pop();
            
            if(head_node == NULL) continue;
            
            q.push(make_pair(head_node -> left, head.second + 1));
            q.push(make_pair(head_node -> right, head.second + 1));
            
            if(q.front().second == head.second)
                head_node -> next = q.front().first;
            else
                head_node -> next = NULL;
        }
        return root;
    }
};