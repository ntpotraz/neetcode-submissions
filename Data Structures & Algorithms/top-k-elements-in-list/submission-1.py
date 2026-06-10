class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for key, value in freq.items():
            buckets[value].append(key)

        res = []
        index = len(buckets) - 1
        while index > -1 and len(res) != k:
            if len(buckets[index]) == 0:
                index -= 1
                continue
            res += buckets[index]
            index -= 1
        return res



        print(buckets)


        
