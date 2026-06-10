class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                pInd, pHeight = stack.pop()
                area = max(area, pHeight * (i - pInd))
                start = pInd
            stack.append((start, height))
        
        for i, height in stack:
            area = max(area, height * (len(heights) - i))

        return area

                


