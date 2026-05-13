class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hash:
                return [hash[comp], i]
            hash[nums[i]] = i
        return []