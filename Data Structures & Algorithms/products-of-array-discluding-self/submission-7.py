class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix, postfix = 1, 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        for i in reversed(range(n)):
            result[i] *= postfix
            postfix *= nums[i]
        return result


        