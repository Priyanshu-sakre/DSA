class Solution:
    # Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        new = Node(x)
        if p + 1 >= self.len1(head):
            current = head
            while current.next:
                current = current.next
            current.next = new
            new.prev = current
        else:
            count = 0
            temp = None
            current = head
            while current and count < p + 1:
                temp = current
                current = current.next
                count += 1
            temp.next = new
            new.next = current
            new.prev = temp
            current.prev = new
        return head

    def len1(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
