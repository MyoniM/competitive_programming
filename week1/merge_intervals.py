class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for i, p in enumerate(intervals):
            if not result: result.append(p)
            elif result[-1][1] >= p[0]: result[-1] = [result[-1][0], max(result[-1][1],p[1])]
            else: result.append(p)
        return result
