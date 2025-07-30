class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        last = matrix[0]
        if target in last:
            return True
        for row in matrix[1:]:
            if row[0] > target:
                if target in last:
                    return True
            else:
                last = row
        if target in last:
            return True
        return False
            