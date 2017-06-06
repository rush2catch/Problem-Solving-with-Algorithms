# Problem: Contains Duplicates
# Difficulty: Easy
# Category: Array/Hash Table
# Leetcode 217: https://leetcode.com/problems/contains-duplicate/#/description
# Description:
"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""


# Solution:
"""
use a hash table to solve; since in python it takes O(n) time to search in dictionary,
the time complexity is O(n)
"""


class Solution(object):

    def contains_duplicate(self, nums):

        if len(nums) < 2:
            return False
        # initialize
        buff_dic = {}

        for i in range(len(nums)):
            if nums[i] in buff_dic:
                # index = [buff_dic[nums[i]], i]
                # print('indices are {}'.format(index))
                return True
            buff_dic[nums[i]] = i
        return False

# test cases:
obj = Solution()
print(obj.contains_duplicate([1, 2, 3, 4, 5]))
print(obj.contains_duplicate([1, 2, 3, 1, 5]))
print(obj.contains_duplicate([]))
print(obj.contains_duplicate([1]))
print(obj.contains_duplicate([1, 2, 3, 2]))
