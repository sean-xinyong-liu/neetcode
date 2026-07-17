class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = max(sum(piles) // h, 1)
        right = max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            t = sum(list(map(lambda x: math.ceil(x / mid), piles)))
            if t <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return res