# Circular Queue Abstract Data Type (ADT)


class CircularQueue(object):

    def __init__(self):
        self.list = []

    def is_empty(self):
        return self.list == []

    def enqueue(self, x):
        self.list.insert(0, x)

    def dequeue(self):
        self.list.insert(0, self.list.pop())

    def size(self):
        return len(self.list)

obj = CircularQueue()
print("isEmpty: {}".format(obj.is_empty()))
print("enqueue 1")
obj.enqueue(1)
print("Circular Queue now is: {}".format(obj.list))
print("enqueue 2")
obj.enqueue(2)
print("Circular Queue now is: {}".format(obj.list))
print("enqueue 3")
obj.enqueue(3)
print("Circular Queue now is: {}".format(obj.list))
print("enqueue 4")
obj.enqueue(4)
print("Circular Queue now is: {}".format(obj.list))
print("enqueue 5")
obj.enqueue(5)
print("Circular Queue now is: {}".format(obj.list))
print("isEmpty: {}".format(obj.is_empty()))
print("Circular Queue now is: {}".format(obj.list))
print("size: {}".format(obj.size()))
print("dequeue")
obj.dequeue()
print("Circular Queue now is: {}".format(obj.list))
print('dequeue')
obj.dequeue()
print("Circular Queue now is: {}".format(obj.list))
print("enqueue 6")
obj.enqueue(6)
print("Circular Queue now is: {}".format(obj.list))
obj.dequeue()
print("dequeue")
print("Circular Queue now is: {}".format(obj.list))
obj.enqueue(7)
print("enqueue 7")
print("Circular Queue now is: {}".format(obj.list))
obj.dequeue()
print("dequeue")
print("Circular Queue now is: {}".format(obj.list))