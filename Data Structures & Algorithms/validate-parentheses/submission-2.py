class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        closing = {"(":")","{":"}","[":"]"}
        stack = []
        for char in s:
            if char in closing:
                stack.append(closing[char])
            else:
                if not stack or char != stack.pop():
                    return False
        return not stack 
