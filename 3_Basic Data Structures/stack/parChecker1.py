from stack import *

def parChecker1(symbolString):
    """
    :param symbolString: target string to parse - list
    :param symbol:       symbols in the sting - char
    :index:              index to locate symbol - int
    :balanced:           flag: boolean
    :s:                  stack
    :return: Boolean
    """
    balanced = True
    index = 0
    s = Stack()
    #symbol = symbolString[index]

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if s.isEmpty() and balanced:
        return True
    else:
        return False


print(parChecker1('(()())(())()'))
print(parChecker1('(((())))()))'))
print(parChecker1('[][]['))
print(parChecker1('(())((())())'))