class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map= {}

        l = 0
        maxF = 0
        res = 0

        for r in range(len(s)):
            map[s[r]] = map.get(s[r], 0) + 1
            maxF = max(map[s[r]], maxF)
            while(r -l + 1) - maxF > k:
                map[s[l]] -=1 
                l+=1
            res = max(res, r - l +1)
        
        return res
        