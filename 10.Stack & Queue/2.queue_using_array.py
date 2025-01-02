class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def enqueue(self, x):
        self.item.append(x)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty cannot dequeue")
            return
        return self.item.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.item[0]

    def size(self):
        return len(self.item)
