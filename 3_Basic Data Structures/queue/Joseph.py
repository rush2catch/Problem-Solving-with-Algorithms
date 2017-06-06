# Joseph's Problem
from Queue import Queue


def joseph(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    print('Initial namelist is : {}'.format(namelist))

    while simqueue.size() > 1:
        for i in range(num - 1):
            simqueue.enqueue(simqueue.dequeue())
        eliminated = simqueue.dequeue()
        print("THe remaining list is : {} and the eliminated one is : {}".format(simqueue.items, eliminated))

    return simqueue.dequeue()

arr = [i for i in range(1, 41)]
print(joseph(arr, 7))
