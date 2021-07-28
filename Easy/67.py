class Solution(object):
    def addBinary(self, a, b):
        a1=int(a,2)
        b1=int(b,2)
        sum = a1+b1
        return '{0:0b}'.format(sum)