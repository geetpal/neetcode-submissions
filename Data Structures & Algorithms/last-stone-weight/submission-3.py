class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x  = heapq.heappop(maxHeap)
            y  = heapq.heappop(maxHeap)

            if x < y:
                heapq.heappush(maxHeap, -1 * (y - x))
            if x == y:
                continue
         
        
        return -1 * maxHeap[0] if maxHeap else 0

      