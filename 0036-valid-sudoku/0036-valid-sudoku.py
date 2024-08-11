class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid_unit(unit):
            unit = [num for num in unit if num != '.']
            return len(unit) == len(set(unit))

        # Check rows
        for row in board:
            if not is_valid_unit(row):
                return False

        # Check columns
        for col in range(9):
            if not is_valid_unit([board[row][col] for row in range(9)]):
                return False

        # Check 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid_unit([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]):
                    return False

        return True