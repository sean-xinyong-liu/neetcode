from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        mono: deque[int] = deque()
        for index, value in enumerate(nums):
            while mono and mono[0] <= index - k:
                mono.popleft()
            while mono and nums[mono[-1]] < value:
                mono.pop()
            mono.append(index)
            if index >= k - 1:
                result.append(nums[mono[0]])
        return result
            
        