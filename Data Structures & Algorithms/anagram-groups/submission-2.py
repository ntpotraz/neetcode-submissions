class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordDict = {}
        res = []

        for i, s in enumerate(strs):
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            if tuple(freq) in wordDict:
                wordDict[tuple(freq)].append(i)
            else:
                wordDict[tuple(freq)] = [i]
        
        for key, value in  wordDict.items():
            group = []
            for v in value:
                group.append(strs[v])
            res.append(group)
        return res

