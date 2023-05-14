from typing import List

class Solution:
    # 我写的垃圾
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        low = 0
        high = len(nums) - 1
        flag = 0

        while(low <= high):
            mid = int((low + high) / 2)
            if(nums[mid] == target):
                result.append(mid)
                flag = 1
                for i in range(mid-1,low-1,-1):
                    if(nums[i] == target):
                        result.append(i)
                    else:
                        break
                for i in range(mid+1,high+1,1):
                    if(nums[i] == target):
                        result.append(i)
                    else:
                        break
                break
            elif(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1

        if(flag == 0):
            return [-1,-1]
        else:
            result.sort()
            if(len(result) == 1):
                result.append(result[0])
            elif(len(result) > 2):
                temp = []
                temp.append(result[0])
                temp.append(result[len(result)-1])
                result = temp
            return result

# 标准答案

# 1、首先，在 nums 数组中二分查找得到第一个大于等于 target的下标leftBorder；
# 2、在 nums 数组中二分查找得到第一个大于等于 target+1的下标， 减1则得到rightBorder；
# 3、如果开始位置在数组的右边或者不存在target，则返回[-1, -1] 。否则返回[leftBorder, rightBorder]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:  # 不变量：左闭右闭区间
                middle = left + (right - left) // 2
                if nums[middle] >= target:
                    right = middle - 1
                else:
                    left = middle + 1
            return left  # 若存在target，则返回第一个等于target的值

        leftBorder = binarySearch(nums, target)  # 搜索左边界
        rightBorder = binarySearch(nums, target + 1) - 1  # 搜索右边界
        if leftBorder == len(nums) or nums[leftBorder] != target:  # 情况一和情况二
            return [-1, -1]
        return [leftBorder, rightBorder]
