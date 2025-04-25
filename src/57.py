class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        ln = len(intervals)

        # add intervals up to a merging point
        while i < ln and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # merge intervals
        while i < ln and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        # add resting intervals
        while i < ln:
            res.append(intervals[i])
            i += 1

        return res
