# coding:utf-8

# problem:
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.

# learn:
# index = 0 <if 0> is false
# remove the dupliacates
# conside [0,0] return None


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d ={nums[i]:i+1 for i in range(len(nums))}
        a = []
        if len(nums) >2:
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        if d.get(-nums[i]-nums[j]) and d.get(-nums[i]-nums[j]) != i+1 and d.get(-nums[i]-nums[j]) != j+1:
                            if nums[i] <= nums[j] and nums[j] <= -nums[i]-nums[j]: 
                                if [nums[i],nums[j],-nums[i]-nums[j]] not in a:
                                    a.append([nums[i],nums[j],-nums[i]-nums[j]])
        else:
            a = []
        return a



s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))