from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化数组
        numbers = [[0 for j in range(n)] for i in range(n)]
        # count记录元素
        count = 1
        # x 和 y 表示起始位置的横坐标和纵坐标
        x = 0
        y = 0
        # offset 表示写完一行后的结尾位置
        offset = 1

        for k in range(int(n/2)):
            for j in range(y,n-offset):
                numbers[x][j] = count
                count += 1
            for i in range(x,n-offset):
                numbers[i][n-offset] = count
                count += 1
            for j in range(n-offset,y,-1):
                numbers[n-offset][j] = count
                count += 1
            for i in range(n-offset,x,-1):
                numbers[i][y] = count
                count += 1
            offset += 1
            x += 1
            y += 1

        if n % 2 == 1:
            numbers[int(n/2)][int(n/2)] = count
        # print(numbers)
        return numbers

# s = Solution()
# s.generateMatrix(4)