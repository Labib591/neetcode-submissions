class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rarr = []
        h = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i])) 
            if key not in h:
                h[key] = []
            h[key].append(strs[i])
        return list(h.values())

        