
def test(nums):
	currentMax = 0
	cursor = 0
	for i in range(len(nums)):
		if nums[i] >= currentMax:
			currentMax = nums[i]
			cursor = i
	return currentMax, cursor

test_list = [1, 3, 4, 6, 2, 9, 11, 2]
print(test(test_list))