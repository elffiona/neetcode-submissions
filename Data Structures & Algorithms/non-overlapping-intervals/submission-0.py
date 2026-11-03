class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        end = float('-inf')
        for i in intervals:
            if i[0] < end:
                # Need to remove
                cnt += 1
            else:
                end = i[1]

        return cnt

        