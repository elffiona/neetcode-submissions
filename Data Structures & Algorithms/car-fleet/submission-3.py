class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed), reverse=True)
        for pos, spd in pairs:
            time = (target - pos) / spd

            if stack and time <= stack[-1]:
                # This car catches the fleet ahead
                continue

            stack.append(time)

        return len(stack)
