class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # this will store the elements in a dictionary
        for i, num in enumerate(nums): # gets the index and the value
            comp = target - num
            # i need to make a if statement to check if the rest of the list + element = sum
            if comp in seen:
                return [seen[comp], i]            
            seen[num] = i # will add the index/value to the dict
