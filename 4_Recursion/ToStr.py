def toStr(n, base):
    convertString = "0123456789ABCDE"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]

print(toStr(1453, 10))

    