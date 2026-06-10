class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = [0] * 26
        tChars = [0] * 26

        for c in s:
            index = ord(c) - ord('a')
            sChars[index] += 1
            
        for c in t:
            index = ord(c) - ord('a')
            tChars[index] += 1
        
        return sChars == tChars
        