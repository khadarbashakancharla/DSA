class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        merged_intervals = []
        for interval in intervals:
            if interval[0] <= end:
                end = max(end,interval[1])
            else:
                merged_intervals.append([start,end])
                start = interval[0]
                end = interval[1]
        merged_intervals.append([start,end])
        return merged_intervals            

        