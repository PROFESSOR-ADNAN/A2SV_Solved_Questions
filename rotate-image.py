class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        left, right = 0, n-1
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1

        
        for r in range(n):
            for c in range(r+1):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        
