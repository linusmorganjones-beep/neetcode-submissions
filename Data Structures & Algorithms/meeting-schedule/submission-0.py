"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals,key=lambda Interval: Interval.start)
        for i in range(1,len(sorted_intervals)):
            current_end = sorted_intervals[i-1].end
            current_start = sorted_intervals[i].start
            if current_end > current_start:
                return False
        
        return True

