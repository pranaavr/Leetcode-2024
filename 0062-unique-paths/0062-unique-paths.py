import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return (math.factorial((m-1)+(n-1))// (math.factorial(m-1)*math.factorial(n-1)))
        
        