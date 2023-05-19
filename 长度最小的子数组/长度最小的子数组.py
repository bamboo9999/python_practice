from typing import List

# 我写的垃圾方法超时了
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # i表示滑动窗口的大小
        flag = 0
        for i in range(1,n+1):
            k = 0
            sum = 0
            while k < n:
                for j in range(i):
                    if(k+j >= n):
                        break
                    sum = sum + nums[k+j]
                    if(sum >= target):
                        flag = 1
                        break
                k = k + 1
                sum = 0
                if(flag == 1):
                    break
            if(flag == 1):
                return i
        if(flag == 0):
            return 0


# 用滑动窗口来做
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # sum表示滑动窗口内元素的和
        sum = 0
        # i表示起始位置
        i = 0
        # result表示滑动窗口最终的长度
        result = n
        flag = 0
        # j代表终止位置
        for j in range(n):
            sum = sum + nums[j]
            # 尝试缩短滑动窗口，所以要用while而不是if
            while(sum >= target):
                flag = 1
                # length表示滑动窗口的长度
                length = j - i + 1
                if (length < result):
                    result = length
                # 起始位置往后移动，sum的值会减小
                sum = sum - nums[i]
                i = i + 1
        if(flag == 0):
            return 0
        else:
            return result