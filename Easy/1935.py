class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        num = len(words)
        for i in words:
            for j in brokenLetters:
                if j in i:
                    num -= 1
                    break
        
        return num