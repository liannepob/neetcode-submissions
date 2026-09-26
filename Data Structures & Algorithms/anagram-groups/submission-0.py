from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # defaultdict(list) checks lists even if empty
        for word in strs:
            count = [0] * 26 # one slot for each letter a-z
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())