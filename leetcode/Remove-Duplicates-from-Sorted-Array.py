# coding: utf-8

# problem:
# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int}
        :rtype: int
        """
        a = len(nums)
        i = 0
        while i < a:
            b = nums[0]
            nums.pop(0)
            if b not in nums:
            	nums.append(b)
            	i = i + 1
            else:
            	a = len(nums)
        return len(nums),nums

nums = [1,2]
s = Solution()
print(s.removeDuplicates(nums))


