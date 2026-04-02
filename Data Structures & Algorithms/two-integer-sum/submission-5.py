class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inde = {}
        for i,num in enumerate(nums):
            inde[num]=i
        for i,num in enumerate(nums):
            need = target - num
            if need in inde and inde[need] != i:
                return [i,inde[need]]