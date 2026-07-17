class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # The maximal rectangle for any bar is determined by the first shorter bar 
        # to its left and right (its boundaries).
        # We maintain a monotonic stack of indices with increasing heights. 
        # We push bars to the stack if they maintain the increasing order.
        # When a shorter bar is encountered, it defines the right boundary for the 
        # taller bars in the stack, triggering us to pop them and calculate their area.
        
        # Add sentinels: 
        # The leading 0 prevents empty stack errors (acts as a universal left boundary).
        # The trailing 0 ensures the stack is fully flushed at the end.
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            # While the current bar breaks the increasing order, resolve areas for popped bars
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()] 
                # Width = Right Boundary (current i) - Left Boundary (new stack top) - 1
                width = i - stack[-1] - 1 
                area = height * width
                max_area = max(area, max_area)
            stack.append(i)
        return max_area