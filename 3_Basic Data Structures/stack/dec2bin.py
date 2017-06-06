from stack import Stack

def dec2bin(decNumber):

    remStack = Stack()
    binString = ''

    if not isinstance(decNumber,int):
        print("args should be integer: .", end = ' ')
        return -1
    elif decNumber < 0:
        print("args should not be negative:", end = ' ')
        return -1
    elif decNumber == 0:
        binString = '0'
    else:
        while decNumber > 0:
            remainder = decNumber % 2
            decNumber = decNumber // 2
            remStack.push(remainder)


    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())

    return binString

print("dec = 0, bin = {}".format(dec2bin(0)))
print("dec = -1, bin = {}".format(dec2bin(-1)))
print("dec = 8, bin = {}".format(dec2bin(8)))
print("dec = 17, bin = {}".format(dec2bin(17)))
print("dec = 21, bin = {}".format(dec2bin(21)))
print("dec = 21939449955959595, bin = {}".format(dec2bin(21939449955959595)))
print("dec = 1.9, bin = {}".format(dec2bin(1.9)))
print("dec = '89', bin = {}".format(dec2bin('89')))


