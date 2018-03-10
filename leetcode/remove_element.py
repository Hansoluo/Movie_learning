# coding: utf-8

# problem:
# Given an array and a value, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# learn:
# list operation : pop(i)  O(1)
# pop(i) can change the length of the list


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a = len(nums)
        i = 0
        while i < a:
            if nums[i] == val:
                nums.pop(i)
                a = len(nums)
            else:
                i = i + 1
        return len(nums)

nums = [0,4,4,0,4,4,4,0,2]
val = 4
s = Solution()
print(s.removeElement(nums,val))



