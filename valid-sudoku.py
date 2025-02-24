# Time O(m*n)
# Space O(3m*n)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for i in range(len(board))]
        col_sets = [set() for i in range(len(board[0]))]
        mat_sets = [set() for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    # Check row
                    if board[i][j] in row_sets[i]: 
                        print("row set",i, j)
                        return False
                    else: row_sets[i].add(board[i][j])
                    # Check column
                    if board[i][j] in col_sets[j]: 
                        print("col set",i, j)
                        return False
                    else: col_sets[j].add(board[i][j])
                    # Check 3x3 matrix
                    k = (3 * (i//3)) + (j//3)
                    if board[i][j] in mat_sets[k]: 
                        print("mat set",i, j)
                        return False
                    else: mat_sets[k].add(board[i][j])
        return True

# Time O(3m*n)
# Space O(m)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row check
        for i in range(len(board)):
            numset = set()
            for j in range(len(board[0])):
                if board[i][j] != ".": 
                    if board[i][j] in numset: 
                        print("row", i, j)
                        return False
                    else: numset.add(board[i][j])
        # Column check
        for j in range(len(board[0])):
            numset = set()
            for i in range(len(board)):
                if board[i][j] != ".": 
                    if board[i][j] in numset: 
                        print("col", i, j)
                        return False
                    else: numset.add(board[i][j])
        # mat 3x3 check
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                numset = set()
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        if board[m][n] != ".":
                            if board[m][n] in numset: 
                                return False
                            else: numset.add(board[m][n])
        return True
