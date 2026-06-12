class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            total = 0
            for p in piles:
                total += math.ceil(p / mid)
            return total <= h

        l, r = 1, max(piles)

        while l <= r:
            total = 0
            mid = (l + r) // 2
            if check(mid):
                 r = mid - 1
            else:
                l = mid + 1

        return l

