class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        td = [0] * 26
        sd = [0] * 26

        for i in range(len(s)):
            sInd = ord(s[i]) - ord('a')
            tInd = ord(t[i]) - ord('a')
            sd[sInd] += 1
            td[tInd] += 1
        
        print(f"td: {td}")
        print(f"sd: {sd}")
        
        return td == sd