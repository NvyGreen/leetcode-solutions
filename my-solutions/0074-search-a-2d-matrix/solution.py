class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1

        while start <= end:
            mid = (start + end) // 2
            r = mid // len(matrix[0])
            c = mid % len(matrix[0])

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                start = mid + 1
            else:
                end = mid - 1
            
        return False
