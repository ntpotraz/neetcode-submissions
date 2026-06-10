class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        right = k

        for left in range(len(nums) - k + 1):
            print(f"left: {left}")
            print(f"right: {right}")
            res.append(max(nums[left:right]))
            right += 1
            
        return res
        