
def selection_sort(nums):

	pos = len(nums) - 1
	loops = len(nums)
	currentMax = 0
	cursor = 0

	for n in range(len(nums)):

		for i in range(loops):
			if nums[i] >= currentMax:
				currentMax = nums[i]
				cursor = i

		nums[cursor] = nums[pos]
		nums[pos] = currentMax

		loops -= 1
		pos -= 1
		currentMax = 0
		cursor = 0
		# print("-"*5,loop_ct,"-"*5)

	return nums

test_list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#print(sorted(test_list_1))
print(test_list_1)
print(selection_sort(test_list_1))