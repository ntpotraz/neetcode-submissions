class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
    
        dic = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dic:
                print(dic)
                return [dic[difference], i]
            dic[nums[i]] = i
            