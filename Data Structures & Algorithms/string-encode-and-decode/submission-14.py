class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += f"{len(s)}#{s}"

        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        j = 0
        while i < len(s):
            if s[j] != "#":
                j += 1
                continue
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
