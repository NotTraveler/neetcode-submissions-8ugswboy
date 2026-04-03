
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        itm = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in itm:
                itm[sortedS]=[]
            itm[sortedS].append(s)
        lst = []
        for value in itm.values():
            lst.append(value)
        return lst