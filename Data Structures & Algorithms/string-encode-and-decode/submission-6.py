class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "nil"
        if strs == [""]:
            return "empty"

        return "|".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "nil":
            return []
        if s == "empty":
            return[""]

        return s.split("|")
