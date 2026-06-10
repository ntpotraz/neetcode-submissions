class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxContainer = 0

        l, r = 0, len(heights) - 1

        while l < r:
            x = heights[l]
            y = heights[r]
            z = r - l
            container = min(x, y) * z
            if container > maxContainer:
                maxContainer = container
            if x > y:
                r -= 1
            else:
                l += 1
        return maxContainer