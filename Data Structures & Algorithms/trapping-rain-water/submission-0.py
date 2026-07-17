class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: 
            return 0
        result = 0
        left, right = 1, len(height) - 2
        left_max, right_max = height[0], height[-1]
        while left <= right:
            if left_max < right_max:
                result += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                result += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return result


