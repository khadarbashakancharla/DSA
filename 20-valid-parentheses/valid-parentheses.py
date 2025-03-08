class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(' : ')', '{' : '}', "[" : ']'
        }

        opening_brackets = ['(','[','{']
        for bracket in s:
            if bracket in opening_brackets:
                stack.append(brackets[bracket])
            elif stack and stack[-1] == bracket:
                stack.pop() 
            else:
                return False
        if stack:
            return False
        return True                
                   

        