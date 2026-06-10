class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numsDict = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in numsDict:
                return [numsDict[difference], i]
            numsDict[num] = i
        
        return []