# to test the indexError when dealing with a null list

# WARNING: NEED TO UNDERSTAND DEEP COPY AND SHALLOW COPY

# situation 1: the input list an empty list, and this will raise an IndexError
#              it is because new_list is an empty list, but function is to attempt to write element[0] or new_list[0]
#              in the first iteration, which does not exist, so it raised an IndexError
# By knowing the reason, we could simply have two ways to fix this error, which are given in s2 and s3 in the following


def test_1(input_list):
    new_list = []
    for i in range(len(input_list)):
        new_list[i] = input_list[i]
        print("list is {}, new_list is {}".format(input_list, new_list))
    return new_list

test_1([1, 2, 3, 4])


# situation 2: allocate enough space for the new_list, which is not significant or meaningful,
#              but at least could be a solution in this case
def test_2(input_list):
    new_list = [0, 0, 0, 0]  # initializing by allocating enough memory
    for i in range(len(input_list)):
        new_list[i] = input_list[i]
        print("list is {}, new_list is {}".format(input_list, new_list))
    return new_list
test_2([2, 3, 4, 5])


# situation 3: better to use append(), which I think allocates memory space dynamically
def test_3(input_list):
    new_list = []
    for i in range(len(input_list)):
        new_list.append(input_list[i])
        print("list is {}, new_list is {}".format(input_list, new_list))
    return new_list
test_3([3, 4, 5, 6])
