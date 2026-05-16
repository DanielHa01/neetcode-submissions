class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or not nums:
            return 0
        res, cur = 1, 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                cur += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                res = max(res, cur)
                cur = 1
        res = max(res, cur)
        return res