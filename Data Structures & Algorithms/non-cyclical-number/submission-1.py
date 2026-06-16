class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        def sumOfSquares(num):
            total = 0
            while num:
                digit = num % 10
                total += digit ** 2
                num = num // 10

            return total


        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = sumOfSquares(n)
            
        return False