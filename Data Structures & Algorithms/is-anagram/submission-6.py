class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        td = {}
        sd = {}

        for i in range(len(s)):
            sd[s[i]] = sd.get(s[i], 0) + 1
            td[t[i]] = td.get(t[i], 0) + 1
        
        print(f"td: {td}")
        print(f"sd: {sd}")
        
        return td == sd
