class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        current_start = None
        result = []
        merge_start, merge_end = intervals[0]
        for (start, end) in intervals[1:]:
            if (start > merge_end):
                # New one
                result.append([merge_start, merge_end])
                merge_start = start
                merge_end = end
            elif (end > merge_end):
                # Merge
                merge_end = end
        result.append([merge_start, merge_end])
        return result
            
        
