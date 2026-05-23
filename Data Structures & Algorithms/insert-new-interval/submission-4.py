class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
        if len(intervals) <= 0:
            return [newInterval]

        res = []

        # []

        start = 0

        hold = newInterval

        for i in range(len(intervals)):
            if hold[1] < intervals[i][0]:
                res.append(hold)
                hold = intervals[i]
                start = i + 1
            else:
                break

        

        for i in range(start, len(intervals)):
            cur = intervals[i]

            if cur[0] > hold[1]:
                res.append(hold)
                hold = cur
            elif cur[1] < hold[0]:
                res.append(cur)
            else:
                left = min(hold[0], cur[0])
                right = max(hold[1], cur[1])
                hold = [left, right]
        
        res.append(hold)
        
        return res
