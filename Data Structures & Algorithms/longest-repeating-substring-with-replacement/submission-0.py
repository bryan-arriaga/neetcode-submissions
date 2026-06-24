class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        map = {}
        res = 0
        maxF = 0

        for r in range(len(s)):
            map[s[r]] = map.get(s[r], 0) + 1
            maxF = max(maxF, map[s[r]])

            while(r - l + 1) - maxF > k:
                map[s[l]] -= 1
                l+= 1

            res = max(r - l + 1, res)
        return res
        