
class Solution(object):
    def split(self, word):
        return [char for char in word]
    
    def canConstruct(self, ransomNote, magazine):
        name = self.split(magazine)
        sum = 0
        
        for i in ransomNote:
            for j in range(len(name)):
                if i == name[j]:
                    sum += 1
                    name.pop(j)
                    break
                    
        if sum == len(ransomNote):
            return True
        else:
            return False