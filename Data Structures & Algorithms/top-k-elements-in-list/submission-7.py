class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        lst = set((sorted(list(freq.values()),reverse = True)[:k]))
        need = []
        for key,value in freq.items():
            if value in lst:
                need.append(key)
        return need