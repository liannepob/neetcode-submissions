class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []


        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in nums:
                for j in range(len(nums)):
                    if nums[j] == difference and i != j:
                        indices.append(i)
                        indices.append(j)
                        return indices
