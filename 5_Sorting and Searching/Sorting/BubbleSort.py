def bubble_sort(nums):
	if len(nums) == 0:
		return None

	for i in range(len(nums) - 1):
		for j in range(len(nums) - 1):
			if nums[j] > nums[j + 1]:
				nums[j], nums[j + 1] = nums[j + 1], nums[j]

	return nums

unsorted_list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort(unsorted_list1))
unsorted_list2 = []
print(bubble_sort(unsorted_list2))


