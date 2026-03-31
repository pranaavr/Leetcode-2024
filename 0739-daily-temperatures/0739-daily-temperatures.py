class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        
        stack = []
        for i, temp in enumerate(temperatures):            
            
            while stack and temp > stack[-1][1]:
                less = stack.pop()
                answer[less[0]] = i - less[0]
            else:
                stack.append((i, temp))

        
        return answer