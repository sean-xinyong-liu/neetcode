class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 4 5 6 1 2
        # 5 6 1 2 3 4
        left, right = 0, len(nums) - 1
        min_val = nums[left]
        while left <= right:
            mid = (left + right) // 2
            min_val = min(min_val, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return min_val