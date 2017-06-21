def shell_sort(ary):
	n = len(ary)
	gap = round(n / 2)
	while gap > 0:
		for i in range(gap, n):
			temp = ary[i]
			j = i
			while( j >= gap and ary[j - gap] > temp):
				ary[j] = ary[j - gap]
				j = j - gap
			ary[j] = temp
		gap = round(gap / 2)
	return ary

test_list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(sorted(test_list_1))
print(shell_sort(test_list_1))