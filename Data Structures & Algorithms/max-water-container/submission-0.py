class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        output_area = 0
        while left < right:
            current_area = (right - left) * min(heights[left], heights[right])
            if heights[left] > heights[right]:
                output_area = max(current_area, output_area)
                right -= 1
            elif heights[left] < heights[right]:
                output_area = max(current_area, output_area)
                left += 1
            else:
                output_area = max(current_area, output_area)
                left += 1
                right -= 1
        return output_area