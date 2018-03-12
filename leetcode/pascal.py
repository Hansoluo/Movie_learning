# coding:utf-8

# problem:
# Given numRows, generate the first numRows of Pascal's triangle.

# learn:
# a.insert(-1,1) 不能实现插到末尾，在尾部加数据用a.append()

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        i = 1
        j = 0
        a = []
        b = []
        while i < numRows+1:
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
        return b

s=Solution()
print(s.generate(5))