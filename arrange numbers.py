import collections
class Queue:
    def __init__(self):
        self.queue = collections.deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]


# Example usage:

queue = Queue()

# Enqueue some items
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue some items
item1 = queue.dequeue()
item2 = queue.dequeue()

# Peek at the next item in the queue
item3 = queue.peek()

# Print the items
print(item1)
print(item2)
print(item3)

