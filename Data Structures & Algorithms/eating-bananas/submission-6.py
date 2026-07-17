class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left <= right:
            mid = (left + right) // 2
            t = sum((pile + mid - 1) // mid for pile in piles)
            if t <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result