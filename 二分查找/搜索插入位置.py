from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        flag = 0

        while(low <= high):
            mid = int((low + high) / 2)
            if(nums[mid] == target):
                flag = 1
                return mid
                break
            elif(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1

        if flag == 0:
            return low