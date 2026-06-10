class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nDict = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            nDict[num] = nDict.get(num, 0) + 1
        for num, freq in nDict.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []

        
        