"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0:
            return 0

        room = [0]  # heap

        max_size = 1
        size = 1

        intervals.sort(key=lambda x:x.start)

        for itv in intervals:

            if itv.start < room[0]:
                heapq.heappush(room, itv.end)
                size += 1
                max_size = max(max_size, size)
            else:
                heapq.heappop(room)
                heapq.heappush(room, itv.end)


        return max_size



        