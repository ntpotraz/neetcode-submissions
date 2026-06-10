class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, amt in count.items():
            freq[amt].append(num)

        print(freq)
        
        index = len(freq) - 1
        while len(res) != k:
            if len(freq[index]) == 0:
                index -= 1
                continue
            for ind in freq[index]:
                res.append(ind)
                if len(res) == k:
                    return res
            index -= 1

        

        