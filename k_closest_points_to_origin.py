class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heapq.heappush(heap, [-sqrt(p[0]**2 + p[1]**2), p])
            if len(heap) == k + 1:
                heapq.heappop(heap)

        return list(map(lambda p: p[1], heap))
