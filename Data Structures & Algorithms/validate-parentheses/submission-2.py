class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        for c in s:
            if c in map:
                # Look at top of stack, and see if it pairs with the current char c
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        # If stack is empty at end, it is valid string
        return True if not stack else False