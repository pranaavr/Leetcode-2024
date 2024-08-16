class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        trapped = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                trapped += max(0, left_max-height[l])
            else:
                r -= 1
                right_max = max(right_max, height[r])
                trapped += max(0, left_max-height[r])
        return trapped