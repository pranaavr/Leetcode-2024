class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = [lower(x) for x in s if x.isalnum()]
        return new == new[::-1]