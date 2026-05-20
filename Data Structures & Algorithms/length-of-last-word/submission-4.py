class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        while i >= 0 and s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

        # cleanS = s.strip()
        # n = len(cleanS)

        # for i in range(n-1, -1, -1):
        #     if cleanS[i] == " ":
        #         return n - i - 1
        # return len(cleanS)
        