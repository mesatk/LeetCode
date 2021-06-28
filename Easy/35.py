class Solution(object):
    def searchInsert(self, nums, target):
        index = 0
        while index < len(nums):
            if(target <= nums[index]):
                return index
            else:
                index += 1
        return index



####    Binary Search    ####

class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) / 2
            
            if(nums[mid] < target):
                low += 1
            else:
                high -= 1
        
        return low