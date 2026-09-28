class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)
        index = 0
        prefix = 1 # being multiplied 
        suffix = 1 # being multiplied 
    

        while index < len(nums):
            results[index] = prefix
            prefix *= nums[index]
            index += 1

        index_2 = len(nums) - 1
        while index_2 >= 0:
           results[index_2] *= suffix
           suffix *= nums[index_2]
           index_2 -= 1

        return results
        """
        needs to enumerate through all of the items in the array
        if the item in the array is equal to the item at i dont use it
        if it is not, then use it

        needs to store a variable for the results
        needs to store a variable for the multiples

        """