class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in mapping.values():  # Opening bracket
                stack.append(ch)
            else:  # Closing bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
        