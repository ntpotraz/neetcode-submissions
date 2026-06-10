class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        if len(nums) > len(nums_set):
            return True
        return False
        