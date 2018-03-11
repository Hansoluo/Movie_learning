# coding: utf-8

# problem:
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# list --> numbers --> list
# 看清楚输入和输出的数据类型


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = 0
        n = 1
        i = 0
        k = 1
        while i < len(digits):
            j = len(digits)-i
            while k < j:
                n = 10 * n
                k = k+1
            s = s + n*digits[i]
            i = i +1
            n = 1
            k = 1
        s = s+1
        convert = [0,1,2,3,4,5,6,7,8,9]
        a = []
        while s//10 > 0:
            a.append(convert[s%10])
            s = s//10
        a.append(convert[s%10])
        x = len(a)
        b = []
        m = 0
        while m< x:
            b.append(a.pop())
            m = m+1
        return b


s = Solution()
print(s.plusOne([1,0,9]))
