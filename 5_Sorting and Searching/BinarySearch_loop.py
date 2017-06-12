# binary search - while loop

def binary_search(nums, item):
    first = 0
    last = len(nums) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if nums[mid] == item:
            found = True
        elif nums[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return found

test_list = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(binary_search(test_list, 7))
print(binary_search(test_list, 27))