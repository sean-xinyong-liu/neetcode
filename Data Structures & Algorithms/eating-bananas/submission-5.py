class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = math.ceil(sum(piles) / h), max(piles)
        result = right
        while left <= right:
            mid = (left + right) // 2
            t = sum(list(map(lambda x: math.ceil(x / mid), piles)))
            if t <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result