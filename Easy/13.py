class Solution(object):
    def romanToInt(self, s):
        
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        num = 0
        index = 0
        while index < len(s):
            if index + 1 >= len(s):
                num += dic[s[index]]
                index += 1
            elif dic[s[index]] >= dic[s[index + 1]]:
                num += dic[s[index]]
                index += 1
            else:
                num += dic[s[index + 1]] - dic[s[index]]
                index +=2
        return num