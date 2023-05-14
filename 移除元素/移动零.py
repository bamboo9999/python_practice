from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast = 0
        slow = 0
        val = 0
        size = len(nums)

        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        # 把剩余的元素改成0
        while slow < size:
            nums[slow] = 0
            slow += 1
