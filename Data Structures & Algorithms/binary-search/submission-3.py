class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right= 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
# Edge Case Analysis:
# 1. Adjacency: When left and right are adjacent, mid defaults to left (integer division). 
#    If target > nums[left], left increments to equal right.
# 2. Convergence: Now left, right, and mid point to the same element.
# 3. Termination: If the target is still not found, the pointers cross (left becomes 
#    greater than right), breaking the while loop condition.
