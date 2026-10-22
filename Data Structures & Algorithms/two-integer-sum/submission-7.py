class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = []

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in nums:
                for j in range(len(nums)):
                    if nums[j] == difference and i != j:
                        results.append(i)
                        results.append(j)
                        return results