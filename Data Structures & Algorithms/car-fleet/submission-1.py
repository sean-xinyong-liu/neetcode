class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleets, last_time = 0, 0
        for pos, s in cars:
            current_time = (target - pos) / s
            if current_time > last_time:
                last_time = current_time
                fleets += 1
        return fleets

    
            