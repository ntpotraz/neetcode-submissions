class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nDict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in nDict:
                return [nDict[diff], i]
            nDict[num] = i
        return []