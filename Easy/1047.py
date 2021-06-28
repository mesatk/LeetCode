class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for i in range(len(s)):
            if (len(stack) == 0):
                stack.append(s[i])
            elif stack[len(stack) - 1] != s[i]:
                stack.append(s[i])
            else:
                stack.pop()
                
        return "".join(stack)