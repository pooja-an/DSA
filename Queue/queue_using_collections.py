from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print('Queue is empty!')
            return
        return self.queue.pop()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
