class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()

        end = len(cleaned) - 1
        beg = 0
        for i in range(len(cleaned)//2):
            if cleaned[beg] != cleaned[end]:
                return False
            else:
                beg += 1
                end -= 1
        return True