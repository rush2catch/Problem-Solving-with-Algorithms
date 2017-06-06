# Palindrome Checker

from Deque import Deque


def palindrome_checker(alist):
    p = Deque()

    # deal with a null list
    if len(alist) == 0:
        return None

    # add each element into the queue
    for item in alist:
        p.addRear(item)

    # initialize the flag
    flag = True

    # if the list has only one element, it's not palindrome
    if len(p.items) <= 1:
        flag = False
    # compare the head and the rear
    while len(p.items) > 1 and flag is True:
        if p.removeFront() == p.removeRear():
            flag = True
        else:
            flag = False

    if flag is True:
        return True
    else:
        return False

print(palindrome_checker('lsdkjfskf'))
print(palindrome_checker('radar'))
print(palindrome_checker('aa'))
print(palindrome_checker('a'))
print(palindrome_checker('aba'))
