class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}        # Create dictionary
        for i, num in enumerate(nums):      # keep number and index
            if (target - num) in dic:       # if the completing number is in the dic
                return [dic[target - num], i]   # first the index of the number in the dic
            else:   
                dic[num] = i    #if the completing number is not in the dic, add 