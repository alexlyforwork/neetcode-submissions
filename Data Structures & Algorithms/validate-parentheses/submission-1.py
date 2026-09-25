class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"(":")","{":"}","[":"]"}
        stack = []
        for char in s:
            if char in closing:
                stack.append(closing[char])
            else:
                if not stack or char != stack.pop():
                    return False
        return False if stack else True
