# BRUTE
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 1
        while current and count < (self.len1(head) // 2) + 1:
            current = current.next
            count += 1
        return current


    def len1(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
# OPOTIMAL
# TORTOISE AND HARE METHOD
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
