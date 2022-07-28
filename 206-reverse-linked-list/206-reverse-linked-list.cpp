/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==nullptr) return nullptr;
        
        ListNode *next_node, *previous=nullptr, *current = head;
        while(current != nullptr){
            next_node = current->next;
            current->next = previous;
            previous=current;
            current=next_node;
        }
        
        return previous;
    }
};