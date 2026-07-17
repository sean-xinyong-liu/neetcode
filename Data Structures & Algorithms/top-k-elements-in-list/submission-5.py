class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        result = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                result.append(n)
                k -= 1
                if k == 0:
                    return result




