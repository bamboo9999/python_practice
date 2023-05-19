from typing import List

# 我写的垃圾
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

# 双指针法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        k = n - 1
        j = n -1
        i = 0
        while i<=j:
            if(nums[i] * nums[i] <= nums[j] * nums[j]):
                result[k] = nums[j] * nums[j]
                j -= 1
            else:
                result[k] = nums[i] * nums[i]
                i += 1
            k -= 1
        return result