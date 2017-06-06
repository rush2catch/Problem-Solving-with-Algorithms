# Stack Abstract Data Type (ADT)

# Stack() creates a new stack that is empty.
#    It needs no parameters and returns an empty stack.
# push(item) adds a new item to the top of the stack.
#    It needs the item and returns nothing
# pop() removes the top item from the stack.
#    It needs no parameters and returns the item. The stack is modified.
# peek() returns the top item from the stack but does not remove it.
#    It needs no parameters. The stack is not modified.
# isEmpty() tests to see whether the stack is empty.
#    It needs no parameters and returns a boolean value.
# size() returns the number of items in the stack.
#    It needs no parameters and returns an int. 

class Stack(object):
    def __init__(self):
    #@initialize the Data structure
        self.items = []

    def isEmpty(self):
    #@rtype: boolean
        return self.items == []

    def push(self,item):
    #@type item:int
    #@rtype: void
        self.items.append(item)

    def pop(self):
    #@rtype: int
        return self.items.pop()

    def peek(self):
    #@rtype:int
        return self.items[len(self.items)-1]

    def size(self):
    #@rtype: int
        return len(self.items)

if __name__ == "__main__":
    obj = Stack()
    print("obj is initialized as: ",obj.items)
    obj.push(1)
    obj.push(9)
    obj.push(5)
    obj.push(16)
    obj.push(3)
    print("After several pushes: ",obj.items)
    print("Now is empty? ",obj.isEmpty())
    print("Now the peek is: ",obj.peek())
    print("the size is:", obj.size())
    obj.pop()
    obj.pop()
    
    print("After several pushes: ",obj.items)
    print("Now is empty? ",obj.isEmpty())
    print("Now the peek is: ",obj.peek())
    print("the size is:", obj.size())
