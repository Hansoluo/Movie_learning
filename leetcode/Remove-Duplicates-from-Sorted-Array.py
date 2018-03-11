# coding: utf-8

# problem:
# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# learn:
# 区分两种情况：有重复和无重复的处理
# 调试多考虑基础情况如[1,2],[1,1,1],[1,1,2]

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int}
        :rtype: int
        """
        a = len(nums) - 1
        i = 0
        while i < a:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                a = len(nums) - 1
            else:
                i = i+1
        return len(nums), nums


nums = [1,1,1]
s = Solution()
print(s.removeDuplicates(nums))


