class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # how would you add 1 to count[char] each time you see it?

    # hint: what if the char isn't in the dict yet?        
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        if count_s != count_t:
            return False
        else:
            return True

