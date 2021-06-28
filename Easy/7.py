class Solution(object):
    def reverse(self, x):
        print(x)
        s = str(x)
        a = 0
        b = 1
        if s[0] == "-":
            b = -1
            s = s[1:]
        for i in range(len(s)):
            a += int(s[len(s) - i - 1]) * (10 ** (len(s) - i - 1))
        
        if a * b > 2 ** 31 - 1 or a * b < (-2) ** 31:  
            a = 0
        return a * b