class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_dict = {}

        for i, word in enumerate(strs):
            freq = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                freq[index] += 1
            tup = tuple(freq)
            if tup in freq_dict:
                update = freq_dict[tup]
                update.append(word)
                freq_dict[tup] = update
            else:
                freq_dict[tup] = [word]

        return list(freq_dict.values())

