class Solution:
    def delete_node(self, head, x):
        if x == 1:
            head = head.next
            head.prev = None
            return head
        elif x >= self.len1(head):
            current = head
            while current.next:
                current = current.next
            current.prev.next = None
            return head
        else:
            count = 1
            current = head
            temp = None
            while current and count < x:
                temp = current
                current = current.next
                count += 1
            temp.next = current.next
            current.next.prev = temp
            return head

    def len1(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
