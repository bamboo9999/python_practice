from collections import Counter
from typing import List


# 我写的垃圾超时了
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        result = -1
        # i是起始位置，j是终止位置
        i = 0
        # 记录滑动窗口的起始位置
        for j in range(n):
            # 滑动窗口内的元素
            temp = fruits[i:j+1]
            length = len(temp)
            while(len(set(temp)) > 2):
                i = i + 1
                temp = fruits[i:j+1]
                length = len(temp)
            if(length > result):
                result = length
        print(result)
        return result

# 哈希表 + 滑动窗口
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 是一个计数器，记录每个元素出现的次数，用字典存储
        # cnt是一个字典
        cnt = Counter()

        left = ans = 0
        # enumerate返回的right是元素的下标，x为列表元素的值
        # 右指针一直遍历下去
        for right, x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt) > 2:
                # 左指针移动
                cnt[fruits[left]] -= 1
                # 如果左指针指向的元素没了，则要删除cnt中对应的键
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            # 取最大值
            ans = max(ans, right - left + 1)

        return ans