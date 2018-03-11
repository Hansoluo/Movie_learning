# coding: utf-8

# problem:
# 输入整数，所有位数+1后，返回整数

# learn:
# 数学中的阶乘和进制都可以使用while语句递归来完成

class Solution:
    def plusOne(self, digits):
        """
        :type digits: int
        :rtype: int
        """
        convert = [0,1,2,3,4,5,6,7,8,9,0]
        a = []
        while digits//10 > 0:
        	a.append(convert[(digits%10 + 1)])
        	digits = digits//10
        a.append(convert[(digits%10 + 1)])
        s = 0
        n = 1
        i = 0
        j = 0 
        while i < len(a):
        	while j < i:
        		n = 10 * n
        		j = j+1
        	s = s + n*a[i]
        	i = i+1
        return s

s = Solution()
print(s.plusOne(129))
