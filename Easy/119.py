class Solution(object):
    def getRow(self, rowIndex):
        pasq = [1]
        
        while rowIndex > 0:
            head = 0
            arr = [1]
            while head + 1 < len(pasq):
                arr.append(pasq[head] + pasq[head + 1])
                head += 1
            arr.append(1)
            pasq = arr
            rowIndex -= 1
        
        return pasq 