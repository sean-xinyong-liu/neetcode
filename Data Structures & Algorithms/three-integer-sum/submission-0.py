class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums) - 1
            while left < right:
                left_value = nums[left]
                right_value = nums[right]
                total = left_value + right_value + value
                
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([value, left_value, right_value])
                    left += 1
                    right -= 1 

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return result