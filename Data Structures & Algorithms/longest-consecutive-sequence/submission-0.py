class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        maxLen = 0

        for n in nums:
            if n - 1 not in hashset:
                streak = 1
                while n + streak in hashset:
                    streak += 1
                maxLen = max(streak, maxLen)
        
        return maxLen
        