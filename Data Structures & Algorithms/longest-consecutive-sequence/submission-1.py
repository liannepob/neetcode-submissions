class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        new_nums = set(nums)

        for num in new_nums:
            if num - 1 not in new_nums:
                length = 1
                while num + length in new_nums:
                    length += 1 
                longest = max(longest, length)

        return longest