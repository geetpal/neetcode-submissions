class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl = len(needle)
        hl = len(haystack)

        for i in range(hl):
            if haystack[i] == needle[0]:
                if haystack[i: i + nl] == needle:
                    return i
        return -1
        