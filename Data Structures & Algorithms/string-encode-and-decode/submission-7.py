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
        for c in s:
            if c == "|":
                res.append(single_str)
                single_str = ""
                continue
            single_str += c
        res.append(single_str)
        return res[1:]
            