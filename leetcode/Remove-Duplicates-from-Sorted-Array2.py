# coding: utf-8

# problem:
# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# learn:
# 可以根据比较的位置任意保留去重的个数

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int}
        :rtype: int
        """
        a = len(nums) - 2
        i = 0
        while i < a:
            if nums[i] == nums[i+2]:
                nums.pop(i)
                a = len(nums) - 2
            else:
                i = i+1
        return len(nums), nums


nums = [1,1,1,1,2,3]
s = Solution()
print(s.removeDuplicates(nums))


