class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # APPEND
    def insert_at_tail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def traverse(self):
        if not self.head:
            print("Doubly LL is empty")
        else:
            current = self.head
            while current:
                print(current.val, end=" ")
                current = current.next
            print()

    def search(self, target):
        current = self.head
        while current:
            if current.val == target:
                print(True)
                return
            else:
                current = current.next
        print(False)

    def len(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert_in_between(self, pos, ele):
        new = Node(ele)
        if pos == 0:
            dll.insert_at_head(ele)
        elif pos >= dll.len():
            dll.insert_at_tail(ele)
        else:
            current = self.head
            count = 0
            previ = None
            while current and count < pos:
                previ = current
                current = current.next
                count += 1
            previ.next = new
            new.prev = previ
            new.next = current
            current.prev = new

    def deleter_head(self):
        if not self.head:
            print("DLL is empty")
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleter_tail(self):
        if not self.head:
            print("DLL is empty")
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    def delete_by_value(self,ele):
        pass


dll = DLL()
dll.traverse()
dll.insert_at_head(100)
dll.traverse()
dll.insert_at_head(50)
dll.traverse()
dll.insert_at_tail(200)
dll.traverse()
print(dll.len())
dll.insert_in_between(2, 500)
dll.traverse()
dll.deleter_head()
dll.traverse()
dll.deleter_tail()
dll.traverse()
