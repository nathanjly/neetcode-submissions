class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        if s == "":
            return True

        for c in s:
            if c in table:
                if stack and table[c] == stack[-1]:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False # if stack empty, string is valid