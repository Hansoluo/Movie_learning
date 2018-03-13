# coding:utf-8

# problem:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# error TLE O(n*n)


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i<len(nums)-1:
        	j = i+1
        	while j< len(nums):
        		if nums[i] + nums[j] == target:
        			return i,j
        		j = j+1
        	i = i+1

s = Solution()
print(s.twoSum([3,2,4,3],6))