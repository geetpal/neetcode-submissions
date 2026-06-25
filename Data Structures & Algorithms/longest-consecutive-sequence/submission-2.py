class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest = 0
        # el = nums[0]
        # for n in num_set:
        #     el = n
        #     count = 1

        #     while el + 1 in num_set:
        #         el += 1
        #         count += 1
        #     longest = max(longest, count)

        for n in num_set:
            if n - 1 not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest


            
                

