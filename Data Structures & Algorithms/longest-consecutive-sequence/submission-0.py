class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0
        for num in numSet:
            count = 0
            if num - 1 in numSet:
                continue
            while num + count in numSet:
                count += 1
            maxCount = max(maxCount, count)
        return maxCount

