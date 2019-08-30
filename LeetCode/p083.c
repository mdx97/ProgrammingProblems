#include <stdio.h>
#include <limits.h>

struct ListNode {
    int val;
    struct ListNode *next;
};
 
struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode *prev, *curr;
    curr = head;
    int val = INT_MAX;
    
    while (curr != NULL) {
        if (curr->val == val) {
            prev->next = curr->next;
            curr->next = NULL;
            curr = prev->next;
        } else {
            val = curr->val;
            prev = curr;
            curr = curr->next;
        }
    }
    
    return head;
}