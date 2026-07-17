class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # For every bar, the largest rectangle it can involve fully is fixed once we 
        # know the its first left and right bar that is shorter than it.
        # We can maintain a monotanic stack that tracks incresing bars. Let the bars
        # come in if it's increasing and pop out shorter bars in the stack when the bar 
        # coming in is not the tallest because for those bars being poped out we already know their
        # left boundary and right boundary.
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()] # to pop everything out at the very end, add a 0 to the end of heights
                width = i - stack[-1] - 1 # to avoid empty list indexing, add a 0 to the beginning of heights 
                area = height * width
                max_area = max(area, max_area)
            stack.append(i)
        return max_area