class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        overallMax = 0

        for num in numSet:
            count = 1
            if (num - 1) in numSet:
                continue
            while num + count in numSet:
                count += 1
            if count > overallMax:
                overallMax = count
        return overallMax
