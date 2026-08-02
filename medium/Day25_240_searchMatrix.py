# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。每列的元素从上到下升序排列。

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        while i < m:
            # 当前行最后一个元素都比 target 小，
            # 当前行不可能包含 target
            if matrix[i][n - 1] < target:
                i += 1

            else:
                # 当前行最后一个元素大于等于 target，
                # 搜索当前行
                for j in range(n):
                    if matrix[i][j] == target:
                        return True

                # 当前行没找到，继续检查下一行
                i += 1

        # 所有行都检查完了，仍然没找到
        return False

