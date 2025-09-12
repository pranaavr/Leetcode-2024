class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        for char in s:
            if not stack:
                stack.append(char)
                continue
            elif char in pairs and stack[-1] == pairs[char]:
                stack.pop()
            else:
                stack.append(char)

        if stack:
            return False
        return True