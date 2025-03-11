class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        merging = []
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(end,interval[1])
            else:
                merging.append([start,end])
                start = interval[0]
                end = interval[1]
        merging.append([start,end])
        return merging        


        