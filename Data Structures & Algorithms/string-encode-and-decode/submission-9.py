class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "&" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        encoded = s
        i = 0
        while len(encoded) > 0:
            if encoded[i] == '&' and encoded[i-1].isnumeric():
                print(s[0:i])
                strLen = int(encoded[0:i]) + 1
                strs.append(encoded[i+1:i+strLen])
                encoded = encoded[i+strLen:]
                print(encoded)
                i = 0
                continue
            i += 1
        return strs

