from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            print('Stack is empty!')
            return        
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print('Stack is empty!')
            return
        return self.stack[-1]


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
