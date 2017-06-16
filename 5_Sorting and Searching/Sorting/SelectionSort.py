
def selection_sort(nums):

	pos = len(nums) - 1
	currentMax = 0
	cursor = 0
	loop_ct = 1
	for n in range(len(nums)):

		for i in range(pos):
			if nums[i] > currentMax:
				currentMax = nums[i]
				cursor = i

		if nums[pos] == currentMax:
			currentMax = nums[pos]
			cursor =
		else:
			nums[cursor] = nums[pos]
			nums[pos] = currentMax
		print("_" * 55)
		print(nums)
		print(currentMax, cursor, pos)
		pos -= 1
		currentMax = 1
		cursor = 0
		# print("-"*5,loop_ct,"-"*5)
		loop_ct += 1
		print(nums)
		print([0,  1,  2,  3,  4,  5,  6,  7,  8])

	return nums

test_list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#print(sorted(test_list_1))
print(test_list_1)
print(selection_sort(test_list_1))