class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i,j in enumerate(nums):
            index[j] = i
        for i,j in enumerate(nums):
            need = target - j
            if (need in index) and (index[need] != i):
                return list([i,index[need]])