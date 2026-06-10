class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_dict = defaultdict(list)

        for i, word in enumerate(strs):
            freq = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                freq[index] += 1
            tup = tuple(freq)
            freq_dict[tup].append(word)

        return list(freq_dict.values())

