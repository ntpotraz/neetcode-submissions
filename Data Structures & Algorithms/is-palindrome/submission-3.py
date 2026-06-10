class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

        check = -1
        for c in s.lower():
            if c not in valid:
                continue
            while s[check].lower() not in valid:
                check -= 1

            if c != s[check].lower():
                print(f"{c} != {s[check].lower()}")
                print(f"check = {check}")
                return False
            check -= 1
        return True