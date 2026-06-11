class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = []
        for c in s.lower():
            if c.isalnum():
                cleanedStr.append(c)

        l, r = 0, len(cleanedStr) - 1

        while l < r:
            if cleanedStr[l] != cleanedStr[r]:
                return False
            l += 1
            r -= 1
        return True


