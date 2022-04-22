class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        top = 0
        right = c-1
        bottom = r-1
        left = 0
        direction = 0
        ans = []
        while left <= right and top <= bottom:
            if direction == 0:
                for i in range(left, right+1):

                    ans.append(matrix[top][i])
                top += 1

            elif direction == 1:
                for i in range(top, bottom+1):
                    ans.append(matrix[i][right])
                right -= 1

            elif direction == 2:
                for i in range(right, left-1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            else:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1

            direction = (direction+1) % 4

        return ans


sol = Solution()
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

print(sol.spirallyTraverse(arr, 4, 4))
