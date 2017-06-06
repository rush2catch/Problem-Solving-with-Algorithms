# Problem: Remove Duplicates from Sorted Array
# Difficulty: Easy
# Category: Array/Two Pointers
# Leetcode 26: https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description
# Description:
"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

"""
Time: O(n)
space: O(n)
"""


class Solution(object):
    def remove_duplicates(self, nums):
        if len(nums) < 0:
            return -1

        curHead = 0

        while curHead < len(nums) - 1:

            if nums[curHead] == nums[curHead + 1]:
                nums.pop(curHead)
            else:
                curHead += 1
        return len(nums)

obj = Solution()
print(obj.remove_duplicates([1, 1, 2, 2]))
print(obj.remove_duplicates([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5]))

