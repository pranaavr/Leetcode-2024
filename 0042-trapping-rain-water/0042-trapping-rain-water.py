class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        maxL = 0
        maxR = 0
        collected = 0
        while l < r:
            maxL = max(height[l], maxL)
            collected += maxL - height[l]

            maxR = max(height[r], maxR)
            collected += maxR - height[r]

            if maxL < maxR:
                l += 1
            else:
                r -= 1

        return collected