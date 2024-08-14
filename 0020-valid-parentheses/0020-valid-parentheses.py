class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        CHARS = {
            '[':']',
            '{':'}',
            '(':')'
        }
        left_chars = []
        
        for c in s:
            if c in CHARS:
                left_chars.append(c)
            elif left_chars and c == CHARS[left_chars[-1]]:
                left_chars.pop()
            else:
                return False
        
        return not left_chars
        