# coding:utf-8

# problem:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# error TLE O(n*n)
# 转换思路，遍历加和转化成查找字典

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d ={nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
        	if d.get(target-nums[i]):
        		return i,d.get(target-nums[i])

s = Solution()
print(s.twoSum([3,2,4,3],6))