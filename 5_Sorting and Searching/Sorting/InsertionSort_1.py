
# same algorithm, but use "stop" to break
def insertion_sort(nums):

	for index in range(1, len(nums)):
		temp = nums[index]
		i = index - 1
		stop = False
		while i < index and i >= 0 and not stop:
			if nums[i] <= temp:
				nums[i + 1] = temp
				stop = True
			if nums[i] > temp:
				nums[i + 1] = nums[i]
			i -= 1
		# nums[i + 1] = temp
	return nums

test_list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(insertion_sort(test_list_1))