class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            buckets[count].append(num)

        res = []
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        