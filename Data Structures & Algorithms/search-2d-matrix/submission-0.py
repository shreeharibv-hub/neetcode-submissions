class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                row = i
                break

        if row == -1:
            return False

        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2

            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True

        return False