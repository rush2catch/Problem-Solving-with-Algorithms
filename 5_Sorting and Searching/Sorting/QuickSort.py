def quick_sort(nums):

	if len(nums) < 2:
		return nums

	lower = []
	equal = []
	larger = []

	for i in range(len(nums)):
		pivot = nums[0]
		if nums[i] == pivot:
			equal.append(nums[i])
		if nums[i] > pivot:
			larger.append(nums[i])
		if nums[i] < pivot:
			lower.append(nums[i])

	return quick_sort(lower) + equal + quick_sort(larger)

test1 = [3, 4, 5, 9, 34, 21, 54, 123, 0, 3, 6]
test2 = [0, 2, 3, 21, 65, 12, 21, 9, 5]
print(quick_sort(test1))
print(quick_sort(test2))