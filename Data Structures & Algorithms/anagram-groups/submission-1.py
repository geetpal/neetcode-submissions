class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create groups by words by character count.
        # the key will be created by list that is made of character count
        # Have an array of size 26 and at each index update the count based on Ascii value
        
        res = defaultdict(list)
        for s in strs:
            charCount = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                charCount[idx] += 1
            if tuple(charCount) in res:
                res[tuple(charCount)].append(s)
            else:
                res[tuple(charCount)].append(s)
        return list(res.values())
            


