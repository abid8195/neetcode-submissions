class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}
        output= []
        for s in strs:
            s1 = "".join(sorted(s))
            if s1 in d1:
                d1[s1].append(s)
            else:
                d1[s1] = [s]
        for d in d1.values():
            output.append(d)
        return output
