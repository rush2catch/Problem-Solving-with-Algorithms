# a recursive method to implement binary search

def binary_search(nums, item):
    if len(nums) == 0:
        return False
    mid = len(nums) // 2
    found = False
    if nums[mid] == item:
        found = True
    elif nums[mid] < item:
        return binary_search(nums[mid+1:], item)
    else:
        return binary_search(nums[:mid-1], item)

    return found

test_list = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(binary_search(test_list, 7))
print(binary_search(test_list, 27))