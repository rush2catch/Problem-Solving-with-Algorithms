"""
Problem: leetcode 155 https://leetcode.com/problems/min-stack/#/description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize the data structure
        :return:
        """
        self.s = []

    def push(self,x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.s.append((x,curMin))

    def pop(self):
        if len(self.s) == 0:
            return None
        self.s.pop()


    def top(self):
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s)-1][0]


    def getMin(self):
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s)-1][1]
