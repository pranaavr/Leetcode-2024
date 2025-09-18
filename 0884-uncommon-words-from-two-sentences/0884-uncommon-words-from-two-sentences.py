class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = []
        s11 = s1.split(" ")
        s22 = s2.split(" ")

        for word in s11:
            if s11.count(word) == 1 and word not in s22:
                count.append(word)
        for word in s22:
            if s22.count(word) == 1 and word not in s11:
                count.append(word)

        return count