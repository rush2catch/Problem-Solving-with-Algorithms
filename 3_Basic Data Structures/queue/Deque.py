# Deque Abstract Data Type (ADT)

# Deque() creates a new queue that is empty.
#    It needs no parameters and returns an empty queue.
# addFront(item) adds a new item to the front of the queue.
#    It needs the item and returns nothing
# addRear(item) adds a new item to the end of the queue.
#    It needs the item and returns nothing
# removeFront() removes the front item from the queue.
#    It needs no parameters and returns the item. The queue is modified.
# removeRear() removes the end item from the queue.
#    It needs no parameters and returns the item. The queue is modified.
# isEmpty() tests to see whether the queue is empty.
#    It needs no parameters and returns a boolean value.
# size() returns the number of items in the queue.
#    It needs no parameters and returns an int.


class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
