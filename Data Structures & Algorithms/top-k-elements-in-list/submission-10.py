class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for (num, freq) in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans