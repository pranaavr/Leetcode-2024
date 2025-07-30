class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for col in range(n):
            matrix.append([])
            for row in range(n):
                matrix[n+col].append(matrix[row][col])
        del matrix[0:n]
        for row in range(n):
            matrix[row] = matrix[row][::-1]

        print(matrix)
        