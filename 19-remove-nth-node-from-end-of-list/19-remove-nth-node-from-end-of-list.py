# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        #move fast pointer, n steps ahead
        for _ in range(n):
            fast = fast.next
        #if fast=none, possible only if n==1
        if not fast:
            return head.next
        
        #moving fast and slow pointer till, fast reaches to end
        #hence, fast will move n+(total length - n) steps ahead
        #slow will move (total lenght-n) steps ahead
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        #hence, slow.next be the pointer to element to be deleted
        #hence , swapping the values
        slow.next = slow.next.next
        return head