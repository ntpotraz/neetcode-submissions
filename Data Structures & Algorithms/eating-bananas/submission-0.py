class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            total = 0
            mid = (l + r) // 2
            for bananas in piles:
                total += math.ceil(bananas / mid)
            if total <= h:
                 r = mid
            else:
                l = mid + 1

        return l

