"""
Problem: leetcode 20 Valid Parentheses https://leetcode.com/problems/valid-parentheses/#/description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

from stack import Stack

def parChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if (( top == '(' and symbol == ')') or ( top == '{' and symbol == '}') or ( top == '[' and symbol == ']')) == False :
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker2('[][[[{](){}][}[['))
print(parChecker2('([]){{()}}'))
print(parChecker2('{[(})]'))