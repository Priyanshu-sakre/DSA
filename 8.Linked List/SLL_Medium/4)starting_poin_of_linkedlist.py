# BRUTE
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        l1 = []
        current = head
        while current:
            if current in l1:
                return current
            l1.append(current)
            current = current.next
        return None


# BETTER
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        l1 = {}
        current = head
        while current:
            if current in l1:
                return current
            l1[current] = 1
            current = current.next
        return None
# OPTIMAL
#TORTIOSE AND HARE METHOD
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast #or return slow
        return None
