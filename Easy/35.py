class Solution(object):
    def searchInsert(self, nums, target):
        index = 0
        while index < len(nums):
            if(target <= nums[index]):
                return index
            else:
                index += 1
        return index