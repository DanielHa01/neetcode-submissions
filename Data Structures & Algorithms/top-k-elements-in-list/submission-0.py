class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        return [item[0] for item in sorted(hash.items(), key=lambda item: item[1], reverse=True)][:k]