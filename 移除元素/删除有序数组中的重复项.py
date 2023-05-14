from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 1
        slow = 1
        val = nums[0]
        size = len(nums)

        while fast < size:
            if nums[fast] != val:
                val = nums[fast]
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow