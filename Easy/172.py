class Solution(object):  
    def root(self, fact):
        i = 0
        while fact > 0:
            if fact % 5 == 0:
                i += 1
                fact = fact / 5
            else:
                break
        return i
    
    def trailingZeroes(self, n):
        result = 0
        for i in range(1,n+1):
            if i % 5 == 0:
                result += int(self.root(i))
        return result