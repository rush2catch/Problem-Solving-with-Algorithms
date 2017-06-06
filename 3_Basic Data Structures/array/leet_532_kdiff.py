# Problem: K-diff Pairs in an Array
# Difficulty: Easy
# Category: Array/Two Pointers
# Leetcode 532: https://leetcode.com/problems/k-diff-pairs-in-an-array/#/description
# Description:
"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j),
where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""


# Solution:


class Solution(object):

    # an ugly brute force method...
    def kdiff(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2:
            return -1

        buff_list = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    if nums[i] <= nums[j]:
                        buff_list.append((nums[i], nums[j]))
                    else:
                        buff_list.append((nums[j], nums[i]))
        # print(buff_list)
        # print(set(buff_list))
        return len(set(buff_list))

obj = Solution()
print(obj.kdiff([3, 1, 4, 1, 3, 5], 2))
print(obj.kdiff([1, 2, 3, 4, 5], 1))
print(obj.kdiff([1, 3, 1, 5, 4], 0))
print(obj.kdiff([3, 1, 4, 1, 5], 2))