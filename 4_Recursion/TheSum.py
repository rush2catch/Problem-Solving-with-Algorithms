# use for loops
def list_sum_0(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum


# use recursion
def list_sum_1(numList):
    theSum = 0
    if len(numList) is 0:
        return 0
    elif len(numList) == 1:
        theSum = numList[0]
    else:
        theSum = numList[0] + list_sum_1(numList[1:])
    return theSum

testList = [1, 3, 5, 7, 9]
print(list_sum_0(testList))
print(list_sum_1(testList))

