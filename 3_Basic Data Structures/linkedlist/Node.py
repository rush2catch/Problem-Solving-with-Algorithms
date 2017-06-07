class Node(object):
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

obj1 = Node(93)
print(obj1.get_data())
print(obj1.next)
obj1.set_data(39)
print(obj1.get_data())

obj2 = Node(19)
print(obj2)
print(obj2.next)
print(obj2.get_data())
obj1.set_next(obj2)
print(obj1.next)


