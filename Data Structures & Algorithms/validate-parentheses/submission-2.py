class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue
            if c == ')' or c == ']' or c == '}':
                if len(stack)!= 0 and stack[-1] == match[c]:
                    stack.pop()
                    continue
                else:
                    return False
        return stack == []
                
                    
            
            
                