class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(ch for ch in s if ch.isalnum()).lower()
        
        n = len(clean_str)
        if n == 0:
            return True
        
        i = 0
        while (i < n // 2):
            if clean_str[i] != clean_str[n - i - 1]:
                return False
            i += 1
        return True