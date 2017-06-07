from Node import Node

class UnorderedLlist(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # since the is list is unordered, we just add the new node at the head
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() is item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        if current is None:
            return None
        while not found:
            if current is None:
                return None
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



obj1 = UnorderedLlist()
print(obj1.isEmpty())
obj1.add(1)
obj1.add(2)
print(obj1.size())
obj1.add(4)
obj1.add(5)
print(obj1.size())
print(obj1.search(3))
obj1.remove(3)
print(obj1.remove(4))
print(obj1.size())
print(obj1.search(4))
obj1.add(6)
obj1.add(7)
print(obj1.size())
print(obj1.search(6))
print(obj1.search(7))
obj1.remove(6)
print(obj1.size())
print(obj1.search(6))
