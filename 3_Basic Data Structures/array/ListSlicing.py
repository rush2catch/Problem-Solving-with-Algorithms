def list_slicing(nums, row, col):
    new_matrix = []
    minimal = row * col
    if nums is []:
        return None
    elif (len(nums) % minimal is 0) and (len(nums) >= minimal):
        for r in range(row):
            new_matrix.append(nums[r * col : (r + 1) * col])
        return new_matrix
    else:
        return nums

list_0 = [1, 2, 3, 6]
print(list_slicing(list_0, 1, 4))
print(list_slicing(list_0, 2, 4))

list_1 = [1, 2, 4, 5, 6, 9, 4, 6, 5, 8, 1, 4]
print(list_slicing(list_1, 3, 4))
print(list_slicing(list_1, 4, 3))
print(list_slicing(list_1, 2, 6))
print(list_slicing(list_1, 6, 2))
print(list_slicing(list_1, 5, 3))
print(list_slicing(list_1, 2, 5))
