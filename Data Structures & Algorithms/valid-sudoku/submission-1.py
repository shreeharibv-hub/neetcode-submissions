class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            seen = set()

            for j in range(9):
                value = board[i][j]

                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)

        # Check columns
        for i in range(9):
            seen = set()

            for j in range(9):
                value = board[j][i]

                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)

        # Check 3 x 3 boxes
        for r_b in range(0, 9, 3):
            for c_b in range(0, 9, 3):

                seen = set()

                for i in range(r_b, r_b + 3):
                    for j in range(c_b, c_b + 3):

                        value = board[i][j]

                        if value != ".":
                            if value in seen:
                                return False
                            seen.add(value)

        return True

obj=Solution()
p=obj.isValidSudoku(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]])
print(p)

