def test(nums, item):
    if len(nums) == 0:
        return False
    first = 0
    last = len(nums)
    mid = (first + last) // 2
    print(len(nums))
    print(mid)
    print(nums)
    print('-'*50)

    if nums[mid] == item:
        return True
    else:
        return test(nums[mid+1:], item)

test_list = [1,3,4,5,6,7,9,10]
print(test(test_list, 11))