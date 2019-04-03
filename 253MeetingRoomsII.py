
a = [1,2,3,4,5,6]
a.pop(-1)
print(1)
















# class Solution:
#     def minMeetingRooms(self, intervals):
#         intervals.sort(key=lambda x:x.start)
#         heap = []  # stores the end time of intervals
#         if len(intervals) == 1:
#             return 1
#         for i in intervals:
#             if heap and i.start >= heap[0]: 
#                 # means two intervals can use the same room
#                 heapq.heapreplace(heap, i.end)
#             else:
#                 # a new room is allocated
#                 heapq.heappush(heap, i.end)
#         return len(heap)