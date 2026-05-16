class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        temp, res = [], 0 
        while r < len(s):
            if s[r] not in temp:
                temp.append(s[r])
                res = max(res, len(temp))
                r += 1
            elif r != l:
                temp.pop(0)
                l += 1
            else:
                l += 1
                r += 1
        return res