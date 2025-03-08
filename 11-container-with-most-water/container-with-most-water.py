class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_are = 0
        while left < right:
            l = min(height[left],height[right])
            b = right - left
            max_are = max(max_are,l*b)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_are           