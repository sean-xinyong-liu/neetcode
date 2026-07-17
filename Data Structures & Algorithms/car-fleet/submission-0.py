class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        timestamp = []
        for pair in sorted(pairs)[::-1]:
            time = (target - pair[0]) / pair[1]
            if not timestamp or time > timestamp[-1]:
                timestamp.append(time)
        return len(timestamp)
            