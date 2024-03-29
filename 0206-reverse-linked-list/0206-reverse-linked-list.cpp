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
        ListNode* prv = NULL;
        ListNode* cur = head;
        while(cur!=NULL){
            ListNode* forward = cur->next;
            cur->next = prv;
            prv = cur;
            cur = forward;
            
        }
        return prv;
    }
};