from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.counts[(point[0], point[1])] += 1
        

    def count(self, point: List[int]) -> int:
        cnt = 0
        x1, y1 = point
        # Loop and check for possible diagnol 
        for (x2, y2), c in self.counts.items():
            # TODO 1: Check if valid diagonal
            # abs(x2-x1) == abs(y2-y1) > 0
            if abs(x2 - x1) == abs(y2 - y1) and abs(y2 - y1) > 0:

                # TODO 2: Find the other two vertices
                other1 = (x2, y1)
                other2 = (x1, y2)

                if other1 in self.counts and other2 in self.counts:

                    # TODO 3: Multiply frequencies and add to cnt
                    cnt += c * self.counts[other1] * self.counts[other2]

        return cnt


        
