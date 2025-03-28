from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            midd = (low + high) // 2
            if nums[midd] == target:
                return midd
            elif target > nums[midd]:
                low = midd+1
            else:
                high = midd-1
        if nums[high] == target:
            return high
        elif nums[high] > target:
            if high < 0:
                return 0
            return high-1
        else:
            return high + 1