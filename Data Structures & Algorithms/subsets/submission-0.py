class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [] 
        results = [] 

        def subset_check(index): 
            if index == len(nums):
               results.append(subset.copy())
               return

            subset.append(nums[index])
            subset_check(index + 1) 
            subset.pop()  
            subset_check(index + 1) 

        subset_check(0)
        return results

            



                


"""
-----------------------------STEP BY STEP--------------------------------

"next: figure out if nums needs to be passed into the recursive call or if it can just be referenced from outside." That way tomorrow's 40 min starts right where this one ended instead of re-deriving it

Check the base case (is index == len(nums)? if so, save a copy and return)
If not, add nums[index] to the subset (include)
Recurse with index+1
Once that recursive call fully returns, pop the element you just added
Recurse again with index+1 (exclude), nothing added this time

Notes:
    - I am given a set of integers
    - I need to return all possible SUBSETS from the set
    - The solution needs to return SETS, order does not matter

Hint Notes:
    1) It should always include an empty element
    array_a = []
    RETURNS: []
    array_b = [1]
    RETURNS: [] [1]

    why? There will always be an implied empty element even when there are just 1 elements in the given nums array

    2)Need to take in account the amount of combinations/subsets that can happen in just 1 set of numbers
    [1,2,3] = [1][1,2][2,3][3,1] etc.
     - but no matter what there will never be any repeats
     - unsure of what glgorithm can help generte all subsets
     ---- guess -----
     it could be a recursive function to count the different subsets and make new ones each tie and then record it 

    3) backtracking can be used to generate subsets
    - iterate through an array using backtracking(DFS??)
    - procwss wach index, adding hte element to the subset and continuing
    - then if not we will not add the element and increase the subset
    BASE CASE:
    - Track the index of the array
    - Track the subset being recorded and worked on

    4)When the index reaches i at the end of the array, add the copy of the subset to an array
    - Needs to iterate from left to right in the array and dont pick an element more than once

    - Needs to have a DFS LIFO algorithm   
    - Pop the elements until [], but recording eahc one at a time
"""