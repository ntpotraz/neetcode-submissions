class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
        new_s = ""
        for c in s.lower():
            if c in valid:
                new_s += c
        

        check = -1
        for c in new_s:
            if c != new_s[check]:
                return False
            check -= 1
        return True