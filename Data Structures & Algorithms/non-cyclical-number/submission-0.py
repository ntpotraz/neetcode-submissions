class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:
            total = 0
            for c in str(n):
                total += int(c) ** 2
            n = total
            if n in seen:
                return False
            seen.add(n)
        
        return True
