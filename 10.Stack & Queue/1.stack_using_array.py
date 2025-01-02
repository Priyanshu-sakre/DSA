class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def push(self, x):
        self.item.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack is empty cannot pop")
            return
        return self.item.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.item[-1]

    def size(self):
        return len(self.item)


st = Stack()
st.push(1)
print(st.pop())
print(st.item)
