class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zcols = []
        for r in range(len(matrix)):
            i = len(zcols)
            for c in range(len(matrix[r])):
                curr = matrix[r][c]
                if curr == 0:
                    zcols.append(c)
            if i != len(zcols):
                matrix[r] = [0]*len(matrix[r])
        print(matrix)
        print(zcols)
        for r in range(len(matrix)):
            for zcol in zcols:
                matrix[r][zcol] = 0

        