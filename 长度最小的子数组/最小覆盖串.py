import collections
from collections import Counter

# 受不了了，写的程序天天超时
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter()
        result = s
        i = 0
        flag = 0
        t_c = Counter()
        for k,v in enumerate(t):
            t_c[v] += 1
        if(len(s) < len(t)):
            return ""
        for index,value in enumerate(s):
            c[value] += 1
            while all(char in c and t_c.get(char) <= c.get(char) for char in t):
                flag = 1
                temp = s[i:index + 1]
                c[s[i]] -= 1
                if(c[s[i]] == 0):
                    c.pop(s[i])
                if(len(temp) <= len(result)):
                    result = temp
                i = i + 1
        if(flag == 0):
            result = ''
        print(result)
        return result

# 别人用滑动窗口写的
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need记录当前滑动窗口下，还需要的元素
        # 如果当滑动窗口包含了某个元素，那么need中该元素的数量减1；如果移除了某个元素，那么need中该元素的数量加1
        need = collections.defaultdict(int)
        # 用t初始化need
        for c in t:
            need[c] += 1
        # 为了防止时间复杂度过高，needCnt用来判断滑动窗口是否包含了T中所有元素
        needCnt = len(t)
        i = 0
        # 表示0到正无穷
        res = (0, float('inf'))

        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1

            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:
                    c = s[i]
                    # 步骤二：增加i，排除多余元素
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)

                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1

        # 如果res始终没被更新过，代表无满足条件的结果
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]

# 题解
# https://leetcode.cn/problems/minimum-window-substring/solutions/258513/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/