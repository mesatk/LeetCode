class Solution(object):
    def findNumbers(self, nums):
        res = 0
        for i in nums:
            word = str(i)
            if len(word) % 2 == 0:
                res += 1
        return res