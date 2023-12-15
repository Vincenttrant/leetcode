class Solution(object):
    def searchMatrix(self, matrix, target):
        l1, r1 = 0, len(matrix) - 1
        l2, r2 = 0, len(matrix[0]) - 1

        while l1 <= r1:
            m1 = r1 - l1 // 2
            m2 = r2 - l1 // 2

            if target not in matrix[m1]:
                if matrix[m1][0] < target:
                    l1 = m1 + 1
                elif matrix[m1][-1] > target:
                    r1 = m1 - 1

            if target in matrix[m1]:
                if matrix[m1][m2] < target:
                    l2 = m2 + 1
                elif matrix[m1][m2] > target:
                    r2 = m2 - 1
                else:
                    return True
        return False