from collections import deque


class Stack:
    def __init__(self):
        self.item = deque()

    def is_empty(self):
        return len(self.item) == 0

    def push(self, x):
        self.item.append(x)
        for _ in range(len(self.item) - 1):
            self.item.append(self.item.popleft())

    def pop(self):
        if self.is_empty():
            print("Stack is empty cannot pop")
            return
        return self.item.popleft()

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.item[0]

    def size(self):
        return len(self.item)


st = Stack()
st.pop()
st.top()
st.push(10)
st.push(20)
st.push(30)
print(st.item)
print(st.pop())
print(st.top())
