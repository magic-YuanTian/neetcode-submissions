class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1

        cur_max = 0

        while left <= right:
            
            cur = min(heights[left], heights[right]) * (right - left)
            cur_max = max(cur, cur_max)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return cur_max
        