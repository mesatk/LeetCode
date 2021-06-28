class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        p = ""
        for i in range(len(s)):
            p += s[len(s) - i - 1]
            
        if s == p:
            return True
        else:
            return False