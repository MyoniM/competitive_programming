class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap=[]
        for i in nums: heapq.heappush(heap, int(i)*-1)
        for i in range(k-1): heapq.heappop(heap)
        return str(heap[0]*-1)
