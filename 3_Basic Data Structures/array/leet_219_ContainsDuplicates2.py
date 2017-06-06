# Problem: Contains Duplicates II
# Difficulty: Easy
# Category: Array/Hash Table
# Leetcode 219: https://leetcode.com/problems/contains-duplicate-ii/#/description
# Description:
"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.
"""

# Solution:
class Solution(object):

    def contains_duplicate(self, nums, k):
        if len(nums) < 2:
            return [-1, -1]

        buff_dic = {}

        for i in range(len(nums)):
            if nums[i] in buff_dic and i - buff_dic[nums[i]] <= k:
                return [buff_dic[nums[i]], i]
            buff_dic[nums[i]] = i
        return [-1, -1]

# test cases:
obj = Solution()
print(obj.contains_duplicate([1, 2, 3, 4, 5, 1], 5))
print(obj.contains_duplicate([1, 2, 3, 4, 5, 1], 4))
print(obj.contains_duplicate([1, 2, 3, 4, 5, 1], 6))
print(obj.contains_duplicate([1, 2, 3], 2))
print(obj.contains_duplicate([1, 1, 1, 1], 0))
# special case
print(obj.contains_duplicate([1, 2, 1, 0, 3, 4, 5, 6, 7, 1], 9))