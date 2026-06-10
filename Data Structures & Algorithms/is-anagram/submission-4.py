class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sSet, tSet = {}, {}
        sSet, tSet = defaultdict(int), defaultdict(int)

        for c in s:
            sSet[c] += 1
            # sSet[c] = sSet.get(sSet[c], 0) + 1
        for c in t:
            tSet[c] += 1
            # tSet[c] = tSet.get(tSet[c], 0) + 1

        return sSet == tSet
        