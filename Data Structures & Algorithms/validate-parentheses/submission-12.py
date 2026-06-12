class Solution:
    def isValid(self, s: str) -> bool:

        mp = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for c in s:
            if c in mp:
                stack.append(mp[c])
            else:
                if not stack or stack[-1] != c:
                    return False
                else:
                    stack.pop()
        return not stack