class Solution(object):
    def removeDuplicates(self, nums):
        k = len(nums)
        i = 0
        while i < len(nums) - 1:
            if(nums[i] == nums[i + 1]):
                nums.remove(nums[i])
                k -= 1
            else:
                i += 1
        return k
        