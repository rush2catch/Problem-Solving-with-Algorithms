# Queue Abstract Data Type (ADT)

# Queue() creates a new queue that is empty.
#    It needs no parameters and returns an empty queue.
# enqueue(item) adds a new item to the bottom of the queue.
#    It needs the item and returns nothing
# dequeue() removes the top item from the queue.
#    It needs no parameters and returns the item. The queue is modified.
# isEmpty() tests to see whether the queue is empty.
#    It needs no parameters and returns a boolean value.
# size() returns the number of items in the queue.
#    It needs no parameters and returns an int.


class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, x):
        self.items.insert(0, x)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
