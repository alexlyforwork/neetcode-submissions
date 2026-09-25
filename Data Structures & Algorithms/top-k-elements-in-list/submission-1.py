from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minheap = []
        for value, cnt in freq.items():
            heapq.heappush(minheap,(cnt,value))
            if len(minheap)>k:
                heapq.heappop(minheap)
        res=[]
        for i in minheap:
            res.append(i[1])
        return res