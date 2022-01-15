# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        

class Solution:
    
    
    def getLength(self,head):
        count=0
        while head:
            count+=1
            head=head.next
        return count
            
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        current=head
        totalLen=self.getLength(head)
        print(totalLen)
        prev=None
        while count<totalLen-n:
            prev=current
            current=current.next
            count+=1
        if prev==None and current.next==None:
            head=None
        elif prev==None:
            head=current.next
        elif current.next==None:
            prev.next=None
        else:
            prev.next=current.next
        
        return head