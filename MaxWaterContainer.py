class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        maxCap = 0
        while i < j:
            if min(heights[i], heights[j]) * (j-i) > maxCap:
                maxCap = min(heights[i],heights[j])*(j-i)

            if heights[i] < heights[j]:
                i += 1
            else: 
                j -= 1
        return maxCap 
        