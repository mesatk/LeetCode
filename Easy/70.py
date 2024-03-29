class Solution(object):
    memo = {1:1, 2:2}        
    def climbStairs(self, n):
            if n in self.memo:
                return self.memo[n]
            else:
                self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                return self.memo[n]