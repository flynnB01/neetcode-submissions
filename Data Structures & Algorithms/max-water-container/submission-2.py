class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        m = 0

        while left < right:
            d = right - left

            if heights[left] > heights[right]:
                if heights[right] * d > m:
                    m = heights[right] * d
                right -= 1
            else:
                if heights[left] * d > m:
                    m = heights[left] * d
                left += 1
        return m