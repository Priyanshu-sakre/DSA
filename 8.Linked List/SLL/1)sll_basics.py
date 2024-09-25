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
        while current.next:
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
            new.next = current
            prev.next = new

    # LENGTH
    def len(self):
        len1 = 1
        current = self.head
        while current.next:
            len1 += 1
            current = current.next
        print(len1)

    # DELETE HEAD
    def deleter_head(self):
        self.head = self.head.next

    def delete_by_value(self, value):
        current = self.head
        while current.next:
            if current.val == value:
                current.val = current.next.val
                current.next = current.next.next
                break
            current = current.next

    def deleter_tail(self):
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = current.next


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
sll.delete_by_value(350)
print()
sll.traverse()
print()
sll.deleter_tail()
sll.traverse()
print()
sll.deleter_tail()
sll.traverse()
print()
sll.deleter_tail()
sll.traverse()
# sll.search(200)
