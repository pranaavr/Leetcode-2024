class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_water = 0
        
        i, j = 0, len(height)-1
        while i < j:
            water = min(height[i], height[j]) * (j-i)
            if max_water < water:
                max_water = water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_water