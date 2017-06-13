def short_bubble_sort(nums):
	exchanges = True
	passnum = len(nums) - 1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				exchanges = True
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
		passnum -= 1
	return nums

unsorted_list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(short_bubble_sort(unsorted_list1))
unsorted_list2 = []
print(short_bubble_sort(unsorted_list2))