class Solution:
    def isValid(self, s: str) -> bool:
        # if odd number string length, must be false
        if len(s) % 2 == 1:
            return False
        
        stack = []
        for c in s:
            if c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif c == '(':
                stack.append(')')
            else:
                # if current char matches top of stack, pop from stack
                if len(stack) > 0 and c == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        