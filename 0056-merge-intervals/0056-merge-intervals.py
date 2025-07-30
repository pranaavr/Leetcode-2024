class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        new = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0] <= new[-1][1]:
                # Merge: Update the end of the last merged interval to the maximum of the two end points
                new[-1][1] = max(new[-1][1], interval[1])
            else:
                # No overlap, add the current interval as a new merged interval
                new.append(interval)
            
        return new        