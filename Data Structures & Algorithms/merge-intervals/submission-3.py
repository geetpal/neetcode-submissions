class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if not intervals: return []

        # Geetpal's Solution 
        # intervals.sort(key = lambda x: x[0])
        
        # res = []
        # ls = intervals[0][0]
        # le = intervals[0][1]

        # for s, e in intervals[1:]:

        #     if s <= le:
        #         le = max(le,e)
        #     else:
        #         res.append([ls, le])
        #         ls = s
        #         le = e
        
        # res.append([ls, le])
        # return res
        intervals.sort(key = lambda x: x[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

