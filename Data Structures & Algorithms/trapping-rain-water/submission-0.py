class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = [0] * len(height), [0] * len(height)

        l[0] = height[0]
        for i in range(1, len(height)):
            l[i] = max(l[i-1], height[i])
        
        r[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            r[i] = max(r[i+1], height[i])
        
        res = 0
        for i in range(len(height)):
            res += min(l[i], r[i]) - height[i]
        return res
