class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        inserted_intervals = []
        if not intervals:
            inserted_intervals.append(newInterval)
            return inserted_intervals
        length = len(intervals)
        merged_interval = intervals[0][:]
        left, right = intervals[0][:], intervals[length-1][:]
        left_index, right_index = 0, length-1

        while intervals[left_index][0] <= newInterval[0]:
            # left pointer, check if start_i is less or equal to newInterval start_i
            left = intervals[left_index][:]
            left_index += 1

        while intervals[right_index][0] > newInterval[1]:
            # right pointer, check if start_i is greater than or equal to newInterval end_i
            right_index -= 1
            right = intervals[right_index][:]

        if intervals[right_index][1] <= newInterval[1]:
            merged_interval = [left[0], newInterval[1]]
        else:
            merged_interval = [left[0], right[1]]

        for i in range(left_index-1):
            inserted_intervals.append(intervals[i][:])

        inserted_intervals.append(merged_interval)

        for i in range(right_index+1, length):
            inserted_intervals.append(intervals[i][:])

        return inserted_intervals
