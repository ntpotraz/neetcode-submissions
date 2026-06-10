class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:
            left = s[i].lower()
            right = s[j].lower()

            if not left.isalnum():
                i += 1
                continue
            if not right.isalnum():
                j -= 1
                continue
            if left != right:
                print(f"{left} != {right}")
                return False
            i += 1
            j -= 1
        return True

            
