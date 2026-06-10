class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numsDict:
                return [numsDict[difference], i]
            numsDict[nums[i]] = i


        