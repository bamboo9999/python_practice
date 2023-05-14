# # 我写的垃圾
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         val = '#'
#         slow1 = 0
#         fast1 = 0
#         size1= len(s)
#
#         fast2 = 0
#         slow2 = 0
#         size2 = len(t)
#
#         # 计算s
#         while fast1 < size1:
#             if s[fast1] != val:
#                 if(fast1 == 0):
#                     pass
#                 else:
#                     slow1 += 1
#             else:
#                 s = s[:slow1] + s[fast1+1:]
#                 slow1 = 0
#                 fast1 = 0
#                 size1 = len(s)
#
#             # 防止下标越界
#             if size1 == 0:
#                 break
#             fast1 += 1
#             if s[slow1] == val and slow1 == 0:
#                 s = s[slow1+1:]
#                 slow1 = 0
#                 fast1 = 0
#                 size1 = len(s)
#
#         # 计算t
#         while fast2 < size2:
#             if t[fast2] != val:
#                 if(fast2 == 0):
#                     pass
#                 else:
#                     slow2 += 1
#             else:
#                 t = t[:slow2] + t[fast2+1:]
#                 slow2 = 0
#                 fast2 = 0
#                 size2 = len(t)
#
#             # 防止下标越界
#             if size2 == 0:
#                 break
#
#             fast2 += 1
#
#             if t[slow2] == val and slow2 == 0:
#                 t = t[slow2+1:]
#                 slow2 = 0
#                 fast2 = 0
#                 size2 = len(t)
#
#         return s == t

# 别人写的
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        # 记录 # 的个数
        skipS = skipT = 0

        # 从后往前遍历
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                # 类似于删除操作
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            # 字符匹配
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1

        return True