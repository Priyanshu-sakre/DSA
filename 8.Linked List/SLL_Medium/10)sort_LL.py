#BRUTE
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1 = []
        current = head
        while current:
            l1.append(current.val)
            current = current.next
        l1.sort()
        current = head
        count = 0
        while current:
            current.val = l1[count]
            count += 1
            current = current.next
        return head
#OPTIMAL
