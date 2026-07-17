class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        product_except_zero = 1
        for index, num in enumerate(nums):
            if num == 0:
                zeros.append(index)
            else:
                product_except_zero *= num
        if len(zeros) == 0:
            return [product_except_zero // num for num in nums]
        elif len(zeros) == 1:
            return [product_except_zero if num == 0 else 0 for num in nums]
        else:
            return [0 for _ in nums]


        