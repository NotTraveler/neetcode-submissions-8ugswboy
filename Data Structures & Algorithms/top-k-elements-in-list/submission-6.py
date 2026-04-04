class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        need = set((sorted(list(freq.values()),reverse = True))[:k])
        res = []
        for key,value in freq.items():
            if value in need:
                res.append(key)
        return res