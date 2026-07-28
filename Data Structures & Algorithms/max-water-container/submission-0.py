class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxWater = 0
        #maxWater = height(lowest) * distance(end-start)

        while(start < end):
            height = min(heights[start],heights[end])

            water = height * (end-start)
            maxWater = max(water,maxWater)

            if height < heights[end]:
                start += 1
            else:
                end -= 1
        
        return maxWater
