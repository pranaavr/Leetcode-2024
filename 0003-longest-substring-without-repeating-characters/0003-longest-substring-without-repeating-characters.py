class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        longest = ''
        for right in range(len(s)):
            sub = s[left:right]
            if s[right] in sub:
                left = right
            if len(sub) > len(longest):
                longest = sub
            right += 1

        return len(longest)