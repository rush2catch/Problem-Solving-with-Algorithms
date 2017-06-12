# a hash function


def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos])

    return sum % tablesize

s = 'abcde'
size = 7
print(hash(s, size))