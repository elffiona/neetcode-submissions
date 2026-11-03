"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for i in intervals:
            events.append((i.start, 1))   # Meeting starts
            events.append((i.end, -1))    # Meeting ends

        events.sort()

        rooms = 0
        max_rooms = 0

        for time, change in events:
            rooms += change
            max_rooms = max(max_rooms, rooms)

        return max_rooms