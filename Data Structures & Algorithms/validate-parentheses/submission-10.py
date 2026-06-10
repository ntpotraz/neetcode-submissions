class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = { ")": "(", "}": "{", "]": "[" }

        for c in s:
            if c in paren:
                if stack and stack.pop() == paren[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack
