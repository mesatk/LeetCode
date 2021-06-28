class Solution(object):
    def generate(self, numRows):
        pasq = [[1]]
        
        while numRows > 1:
            head = 0
            arr = [1]
            while head + 1 < len(pasq[-1]):
                arr.append(pasq[-1][head] + pasq[-1][head + 1])
                head += 1
            arr.append(1)
            
            pasq.append(arr)
            numRows -= 1
        return pasq