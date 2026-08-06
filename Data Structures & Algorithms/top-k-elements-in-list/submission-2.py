from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1 + frequency.get(num, 0)

        min_heap = []
        
        for num in frequency.keys():
            heapq.heappush(min_heap, (frequency[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        solution = []
        while min_heap:
            solution.append(heapq.heappop(min_heap)[1])
        return solution

        
        