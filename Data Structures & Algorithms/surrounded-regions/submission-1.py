class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        safe = set()
        r, c = len(board), len(board[0])

        # Find boundary O's
        for i in range(r):
            if board[i][0] == "O":
                safe.add((i, 0))

        for j in range(c):
            if board[0][j] == "O":
                safe.add((0, j))

        for i in range(r):
            if board[i][c - 1] == "O":
                safe.add((i, c - 1))

        for j in range(c):
            if board[r - 1][j] == "O":
                safe.add((r - 1, j))

        # BFS from all boundary O's
        q = deque(safe)

        while q:
            i, j = q.popleft()

            # Up
            if i > 0 and board[i - 1][j] == "O" and (i - 1, j) not in safe:
                safe.add((i - 1, j))
                q.append((i - 1, j))

            # Down
            if i < r - 1 and board[i + 1][j] == "O" and (i + 1, j) not in safe:
                safe.add((i + 1, j))
                q.append((i + 1, j))

            # Left
            if j > 0 and board[i][j - 1] == "O" and (i, j - 1) not in safe:
                safe.add((i, j - 1))
                q.append((i, j - 1))

            # Right
            if j < c - 1 and board[i][j + 1] == "O" and (i, j + 1) not in safe:
                safe.add((i, j + 1))
                q.append((i, j + 1))

        # Convert surrounded O's to X
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"