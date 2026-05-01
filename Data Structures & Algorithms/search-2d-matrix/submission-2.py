class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] <= target <= matrix[m][-1]:
                break
            else:
                r = m - 1

        else:
            return False

        left, right = 0, len(matrix[m]) - 1       

        while left <= right:
            mid = (left + right) // 2

            if matrix[m][mid] > target:
                right = mid - 1
            elif matrix[m][mid] < target:
                left = mid + 1                
            else:
                return True

        return False

        #Time: O(log(m * n))
        #Space: O(1)

            



