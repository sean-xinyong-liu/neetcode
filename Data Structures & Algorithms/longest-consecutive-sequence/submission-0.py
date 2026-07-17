class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        for num in nums:
            if not (num - 1) in num_set:
                streak = 1
                while (num + 1) in num_set:
                    streak += 1
                    num += 1
                longest_streak = max(longest_streak, streak)
        return longest_streak


