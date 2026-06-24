class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = Counter(s)
        map2 = Counter(t)

        return map == map2