class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        res = []

        index = 0
        while index < len(s):
            endInt = index
            while s[endInt] != "#":
                endInt += 1
                if endInt >= len(s):
                    return res
            wordLen = int(s[index:endInt])
            index = endInt + wordLen + 1
            res.append(s[endInt+1:endInt+wordLen+1])
        return res
            