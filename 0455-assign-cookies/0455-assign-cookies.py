class Solution:
    def findContentChildren(self, children: List[int], cookies: List[int]) -> int:
        count = 0

        cookies.sort(reverse=True)
        children.sort(reverse=True)

        i = 0
        j = 0
        while i < len(cookies) and j < len(children):
            if cookies[i] >= children[j]:
                count += 1
                i += 1
                j += 1
            else:
                j+=1
             
        return count