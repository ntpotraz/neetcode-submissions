class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sDict = defaultdict(list)

        for i, s in enumerate(strs):
            chars = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                chars[index] += 1
            sDict[tuple(chars)].append(i) 
        
        for ana, words in sDict.items():
            group = []
            for i in words:
                group.append(strs[i])
            res.append(group)
        
        return res