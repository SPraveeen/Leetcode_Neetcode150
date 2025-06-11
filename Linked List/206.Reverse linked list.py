
# Iterative method
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev=head,None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    
#recursive method

class Solution(object):
    def reverseList(self, head):
        def reverse(curr,prev):
            if curr is None:
                return prev
            else:
                next=curr.next
                curr.next=prev
            return reverse(next,curr)
        return reverse(head,None)