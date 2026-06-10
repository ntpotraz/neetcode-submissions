class Solution:
    def isValid(self, s: str) -> bool:
        openBrack = {"(", "{", "["}
        closeBrack = {")", "}", "]"}
        stack = []
        
        if len(s) % 2 == 1:
            return False
        
        for c in s:
            if c in openBrack:
                stack.append(c)
            elif c in closeBrack:
                if len(stack) == 0:
                    return False
                match c:
                    case "}":
                        if stack.pop() != "{":
                            return False
                    case ")":
                        if stack.pop() != "(":
                            return False
                    case "]":
                        if stack.pop() != "[":
                            return False
                    case _:
                        return False

        return len(stack) == 0