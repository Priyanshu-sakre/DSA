class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


class SLL:
    def __init__(self) -> None:
        self.head = None

    # APPEND AT END
    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new

    # TRAVERSING
    def traverse(self):
        if not self.head:
            print("The linked list is empty")
        else:
            current = self.head
            while current:
                print(current.val, end=" ")
                current = current.next

    # SEARCHING
    def search(self, target):
        current = self.head
        while current:
            if current.val == target:
                print(True)
                return
            else:
                current = current.next
        print(False)

    # INSERT AT SPECIFIC POSITION
    def insert(self, ele, pos):
        new = Node(ele)
        if pos == 0:
            new.next = self.head
            self.head = new
        else:
            current = self.head
            prev = None
            count = 0
            while current and count < pos:
                prev = current
                current = current.next
                count += 1
            prev.next = new
            new.next = current

    # LENGTH
    def len(self):
        len1 = 0
        current = self.head
        while current:
            len1 += 1
            current = current.next
        print(len1)

    # DELETE HEAD
    def deleter_head(self):
        if not self.head:
            print("Linked List is empty")
            return
        self.head = self.head.next

    def deleter_tail(self):
        if not self.head:
            print("Linked List is empty")
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def delete_by_value(self, value):
        if not self.head:
            print("Linked List is empty")
            return
        current = self.head
        if current.val == value:
            self.head = current.next
            return

        # Traverse the list to find the value
        while current.next:
            if current.next.val == value:
                current.next = current.next.next
                return
            current = current.next

        print("Value not in linked list")

    def deleter_pos(self, pos):
        if not self.head:
            print("Linked List is empty")
        current = self.head
        count = 0
        prev = None
        while current:
            prev = current
            current = current.next
            if count == pos:
                prev.next = current.next
            count += 1


n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
sll = SLL()
sll.head = n1
n1.next = n2
n2.next = n3
print(n1.val)
print(n1.next.val)
print(n1.next.next.val)
sll.append(400)
print(n3.next.val)
sll.insert(50, 1)
sll.insert(350, 4)
sll.len()
sll.traverse()
print()
sll.deleter_head()
sll.traverse()
print()
sll.delete_by_value(350)
sll.traverse()
print()
sll.deleter_tail()
sll.traverse()
print()
sll.search(300)
# sll.search(200)
sll.delete_by_value(200)
sll.traverse()
