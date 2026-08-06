from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        solution = heapq.nlargest(k, counter.keys(), key=counter.get)

        return solution

        
        