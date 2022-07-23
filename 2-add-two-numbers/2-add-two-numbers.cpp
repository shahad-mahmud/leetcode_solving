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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0, res;
        ListNode *head = nullptr, *current=nullptr;
        
        while(l1 != nullptr && l2 != nullptr){
            res = l1 -> val + l2 -> val + carry;
            carry = res / 10;
            res %= 10;
            
            ListNode *new_node = new ListNode();
            new_node->val = res;
            new_node->next = nullptr;
            
            if (head == nullptr) {
                head = new_node;
                current = head;
            }
            else{
                current -> next = new_node;
                current = new_node;
            } 
            
            l1 = l1 -> next;
            l2 = l2 -> next;
            
        }
        
        if (l2 != nullptr) l1=l2;
        while(l1 != nullptr){
            res = l1 -> val + carry;
            carry = res / 10;
            res %= 10;
            
            ListNode *new_node = new ListNode();
            new_node->val = res;
            new_node->next = nullptr;
            
            if (head == nullptr) {
                head = new_node;
                current = head;
            }
            else{
                current -> next = new_node;
                current = new_node;
            } 
            
            l1 = l1 -> next;
        }
        
        if (carry > 0){
            ListNode *new_node = new ListNode();
            new_node->val = carry;
            new_node->next = nullptr;
            
            if (head == nullptr) {
                head = new_node;
                current = head;
            }
            else{
                current -> next = new_node;
                current = new_node;
            }
        }
        
        return head;
    }
};