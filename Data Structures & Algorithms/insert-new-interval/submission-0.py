class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, interval in enumerate(intervals):

            # Case 1: Completely before newInterval
            if interval[1] < newInterval[0]:
                result.append(interval)

            # Case 2: Completely after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]

            # Case 3: Overlapping
            else:
                # Merge into newInterval
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        # Don't forget newInterval
        result.append(newInterval)

        return result