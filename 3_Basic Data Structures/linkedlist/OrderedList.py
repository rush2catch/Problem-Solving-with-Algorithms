from Node import Node

class OrderedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    # search() in ordered list is different from the unordered.
    # in this case, suppose we have an ascending ordered list, thus once the value in the node we are at is > the target
    # it means that the target is not in this list.
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() is item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
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


# test cases:
obj = OrderedList()
for i in range(10, 0, -1):
    obj.add(i)

pointer = obj.head
while pointer is not None:
    print(pointer.get_data(), end = '->')
    pointer = pointer.get_next()
print(None)
print(obj.size())
print("6:{}, 12:{}".format(obj.search(6), obj.search(12)))
obj.remove(4)
obj.remove(9)
obj.remove(5)
pointer = obj.head
while pointer is not None:
    print(pointer.get_data(), end = '->')
    pointer = pointer.get_next()
print(None)
obj.add(15)
obj.add(8)
obj.add(5)
pointer = obj.head
while pointer is not None:
    print(pointer.get_data(), end = '->')
    pointer = pointer.get_next()
print(None)
