import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))  
        
        result = []
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
    
        return result
        
        
