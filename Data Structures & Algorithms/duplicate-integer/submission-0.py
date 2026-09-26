class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = set()

        for i in nums:
            if i in copy:
                return True
            else:
                copy.add(i)
        return False