class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleanS = s.strip()
        n = len(cleanS)

        for i in range(n-1, -1, -1):
            if cleanS[i] == " ":
                return n - i - 1
        return len(cleanS)
        