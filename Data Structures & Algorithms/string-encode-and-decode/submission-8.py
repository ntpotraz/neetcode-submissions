class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            enc = f"|{s}"
            res += enc
        return res


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = []
        single_str = ""
        for i in range(1, len(s)):
            if s[i] == "|":
                res.append(single_str)
                single_str = ""
                continue
            single_str += s[i]
        res.append(single_str)
        return res
            