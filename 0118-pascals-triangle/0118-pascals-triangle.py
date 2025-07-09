class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for n in range(numRows):
            row =[1]*(n+1)
            if n > 1:
                # sum of every 2 numbers in first row fills the next
                i = 1
                while i < n:
                    last_row = pascal[-1]
                    row[i] = last_row[i-1]+last_row[i]
                    i += 1
            pascal.append(row)
        
        return pascal