class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            
        idx, length, start, end = 0, len(intervals), newInterval[0], newInterval[1]
        while idx<length and intervals[idx][1]<start:
            idx+=1
        beforeIdx = idx

        newStart, newEnd = start, end
        while idx<length and intervals[idx][0]<=newEnd:
            newStart = min(newStart, intervals[idx][0])
            newEnd = max(newEnd, intervals[idx][1])
            idx+=1
        return intervals[:beforeIdx] + [[newStart,newEnd]] + intervals[idx:]