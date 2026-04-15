class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i,j in enumerate(nums):
            count[j] = i
        
        for i in range(len(nums)):
            need = target - nums[i]
            if (need in count) and (i != count[need]):
                return [i,count[need]]