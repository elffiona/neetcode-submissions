class MedianFinder:

    def __init__(self):
        # small: smaller half, max heap simulated with negatives
        self.small = []

        # large: larger half, min heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: add to small
        heapq.heappush(self.small, -num)

        # Step 2: move the largest value in small to large
        largest_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, largest_small)

        # Step 3: keep small the same size as large
        # or exactly one element larger
        if len(self.large) > len(self.small):
            smallest_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_large)

    def findMedian(self) -> float:
        # Odd number of elements
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # Even number of elements
        return (-self.small[0] + self.large[0]) / 2.0
        