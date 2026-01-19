class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        f = len(height) - 1
        
        best = 0
        while s < f:
            vol = min(height[f], height[s]) * (f-s)
            
            if vol > best:
                best = vol
            
            if height[f] > height[s]:
                s += 1
            else:
                f -= 1
        
        return best

