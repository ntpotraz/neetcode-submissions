class Solution:
    def isPalindrome(self, s: str) -> bool:

        check = -1
        for c in s.lower():
            if not c.isalnum():
                continue
            while not s[check].isalnum():
                print("second")
                check -= 1

            if c != s[check].lower():
                return False
            check -= 1
        return True