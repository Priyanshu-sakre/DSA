# BRUTE
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
# BETTER
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        lenA = self.len1(headA)
        lenB = self.len1(headB)
        a = max(lenA, lenB) - min(lenA, lenB)
        current1 = headA
        current2 = headB
        if lenA > lenB:
            diff = lenA - lenB
            for i in range(diff):
                current1 = current1.next
        else:
            diff = lenB - lenA
            for i in range(diff):
                current2 = current2.next
        while current1 and current2:
            if current1 == current2:
                return current1
            current1 = current1.next
            current2 = current2.next

    def len1(self, head):
        current = head
        count = 1
        while current:
            count += 1
            current = current.next
        return count
#OPTIMAL
