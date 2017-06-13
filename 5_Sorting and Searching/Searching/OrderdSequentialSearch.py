# suppose the given list is in an ascending order

# -------------- time complexity analysis -------------- #
# ------------------------------------------------------ #
# |    Case    | Best Case | Worst Case | Average Case | #
# ------------------------------------------------------ #
# |item present| 1         | n          | n/2          | #
# ------------------------------------------------------ #
# |not present | 1         | n          | n/2          | #
# ------------------------------------------------------ #

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos += 1
    return found

testlist = [1, 2, 6, 8, 11, 15, 17, 19, 23, 26]
print(orderedSequentialSearch(testlist, 11))
print(orderedSequentialSearch(testlist, 7))