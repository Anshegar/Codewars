'''
Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Дана двоичная матрица размера m x n, заполненная 0 и 1, 
найдите самый большой квадрат, содержащий только 1, и верните его площадь.

'''

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Если матрица пуста, возвращаем 0
        if not matrix:
            return 0

        # Создаем двумерный массив dp, где dp[i][j] будет хранить размер максимального квадрата,
        # который заканчивается в ячейке (i, j)
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        # Инициализируем максимальный размер квадрата как 0
        max_side = 0

        # Проходим по всем ячейкам матрицы
        for i in range(m):
            for j in range(n):
                # Если текущая ячейка содержит '1'
                if matrix[i][j] == '1':
                    # Если ячейка находится на первой строке или первом столбце,
                    # то размер квадрата равен 1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    # Иначе, размер квадрата равен минимальному размеру квадрата
                    # из ячеек слева, сверху и слева-сверху, плюс 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                    # Обновляем максимальный размер квадрата
                    max_side = max(max_side, dp[i][j])

        # Возвращаем площадь максимального квадрата
        return max_side * max_side
        


s = Solution()
matrix = []
# Output: 1
print(s.maximalSquare(matrix))

matrix = [["0","1"],["1","0"]]
# Output: 1
print(s.maximalSquare(matrix))

matrix = [["0"]]
# Output: 0
print(s.maximalSquare(matrix))

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
print(s.maximalSquare(matrix))