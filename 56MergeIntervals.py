# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        res = []
        for inter in sorted(intervals, key = lambda inter:inter.start):
            if res and inter.start <= res[-1].end:
                res[-1].end = max(inter.end, res[-1].end)
            else:
                res.append(inter)
        return res