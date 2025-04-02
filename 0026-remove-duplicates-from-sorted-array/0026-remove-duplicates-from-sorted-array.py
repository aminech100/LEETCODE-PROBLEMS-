class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        dup = 0
        tmpo = nums[0]
        while i < n-1:
            if tmpo == nums[i+1]:
                nums[i+1] = '_'
                dup += 1
            else:
                tmpo = nums[i+1]
            i += 1
        tmp = n - dup
        idx = 1
        i = 1
        while i < n:
            if nums[i] != '_':
                nums[idx] = nums[i]
                idx += 1
            i += 1
        return tmp