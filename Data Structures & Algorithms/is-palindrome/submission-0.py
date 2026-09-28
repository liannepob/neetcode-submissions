class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""
        for i in s:
            if i.isalnum():
                cleaned += i

        front = 0
        back = len(cleaned) - 1
        while front < back:
            if cleaned[front] != cleaned[back]:
                return False
            front += 1
            back -= 1
        return True

