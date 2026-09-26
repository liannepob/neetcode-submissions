from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        # will create buckets based on the length of the list
        # buckets will create buckets and group numbers based on their   frequencies
        counter = Counter(nums)
        # will create a list {1:3, 2: 3, 3: 4}
        for number, frequency in counter.items():
        # will take each item and sort it in order in the buckets array
            buckets[frequency].append(number)

        k_elements = []

        for index in range(len(nums), 0, -1): # works backwards in the nums list    
            if len(k_elements) < k: # check if the length of elements is less than the frequency asked
                if buckets[index]:
                    k_elements.extend(buckets[index]) # extend keyword will add each inividual item to the k_elements list
        
        return k_elements