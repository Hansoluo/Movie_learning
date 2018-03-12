# coding:utf-8

# problem:
# Given an index k, return the kth row of the Pascal's triangle.
# 0 --> 1

class Solution:
    def generate(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        i = 1
        j = 0
        a = []
        b = []
        while i < rowIndex+2:
        	while j<i and i<3:
        		a.append(1)
        		j=j+1
        	while j<i-2 and i>2:
        		a.append(b[-1][j] + b[-1][j+1])
        		j=j+1
        	if i>2:
        		a.insert(0,1)
        		a.append(1)
        	b.append(a)
        	j=0
        	a=[]
        	i=i+1
        return b[rowIndex]

s=Solution()
print(s.generate(0))