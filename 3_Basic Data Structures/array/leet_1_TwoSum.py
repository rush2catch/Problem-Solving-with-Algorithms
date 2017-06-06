# Problem: Two Sum
# Difficulty: Easy
# Category: Array/Hash Table
# Leetcode 1: https://leetcode.com/problems/two-sum/#/description
# Description:
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):

    # Solution 1
    """
    bruce force search in O(n*2) time
    just use two for loops to search the answer, time complexity O(n*2)
    """

    def two_sum_1(self, nums, target):

        # initialize the answer, if no solution, then return null, null
        ans = ['null', 'null']
        # use two for loops to search the answer,O(n*2) solution
        for i in range(len(nums)):
            temp = target - nums[i]
            for j in range(i, len(nums)):
                if temp == nums[j]:
                    ans = [i, j]
        return ans

    # Solution 2
    """
    use a hash table to solve, in python it is easy to think of dic{}
    time complexity: O(n)
    """

    def two_sum_2(self, nums, target):

        # initialize
        buff_dic = {}

        for i in range(len(nums)):
            if target - nums[i] in buff_dic:
                return [buff_dic[target - nums[i]], i]
            buff_dic[nums[i]] = i
        return [-1, -1]


# test cases:
n_0 = [2, 7, 11, 15]
n_1 = [34, 56, 23, 45, 2, 44, 12, 21]
n_2 = [3, 3, 1, 1, 2, 2]
n_3 = [3, 2, 4]
obj = Solution()
print("Expected [0, 1], actual {}".format(obj.two_sum_2(n_0, 9)))
print("Expected [-1, -1], actual {}".format(obj.two_sum_2(n_0, 11)))
print("Expected [0, 1], actual {}".format(obj.two_sum_2(n_1, 90)))
print("Expected [4, 7], actual {}".format(obj.two_sum_2(n_1, 23)))
print("Expected [0, 1], actual {}".format(obj.two_sum_2(n_2, 6)))
print("Expected [2, 3], actual {}".format(obj.two_sum_2(n_2, 2)))
print("Expected [1, 2], actual {}".format(obj.two_sum_2(n_3, 6)))
print("Expected [1, 2], actual {}".format(obj.two_sum_1(n_3, 6)))

