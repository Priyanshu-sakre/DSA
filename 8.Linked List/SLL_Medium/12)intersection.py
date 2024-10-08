class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1={}
        current=headA
        while current:
            l1[current]=1
            current=current.next
        current=headB
        while current:
            if current in l1:
                return current
            current=current.next
        return None
