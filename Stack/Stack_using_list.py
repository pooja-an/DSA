## Implementing Stack using List




class Stack:

    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)

    def pop(self):
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
s.push(50)

print(s.peek())
print('Pop element: ',s.pop())
print(s.peek())
print('Pop element: ',s.pop())
print(s.peek())
print('Pop element: ',s.pop())
print(s.peek())
print('Pop element: ',s.pop())
print(s.peek())
print('Pop element: ',s.pop())
print(s.peek())
