
def selection_sort(nums):

	pos = len(nums) - 1
	currentMax = 0
	cursor = len(nums)
	for n in range(len(nums)):

		for i in range(pos):
			if nums[i] >= currentMax:
				currentMax = nums[i]
				cursor = i
		nums[cursor] = nums[pos]
		nums[pos] = currentMax
		pos -= 1
		currentMax = 0
		cursor = len(nums)

	return nums

test_list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(sorted(test_list_1))
print(selection_sort(test_list_1))