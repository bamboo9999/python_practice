from typing import List

# 写的垃圾
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m,n 获取matrix的行数和列数
        m,n = len(matrix), len(matrix[0])
        # 圈数
        circle = 1 if n == 1 or m == 2 or n == 2 else int(max(m, n) / 2)
        # 起始位置的横纵坐标
        x = 0
        y = 0
        offset = 1
        numbers = []

        if m == 1:
            numbers = matrix[0]
        else:
            for k in range(circle):
                for j in range(y,n-offset):
                    numbers.append(matrix[x][j])
                for i in range(x,m-offset):
                    numbers.append(matrix[i][n-offset])
                for j in range(n-offset,y,-1):
                    numbers.append(matrix[m-offset][j])
                for i in range(m-offset,x,-1):
                    numbers.append(matrix[i][y])

                x += 1
                y += 1
                offset += 1

            if m == n and m % 2 == 1:
                numbers.append(matrix[circle][circle])
        print(numbers[:m*n])
        return numbers[:m*n]

s =Solution()
s.spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])